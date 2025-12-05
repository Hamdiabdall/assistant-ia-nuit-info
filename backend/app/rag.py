from __future__ import annotations

from typing import List, Dict, Any

import json

import numpy as np

from . import config
from .models import SourceFAQ


_faqs: List[Dict[str, Any]] | None = None
_embeddings_matrix: np.ndarray | None = None


def _load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def _hash_string(text: str) -> int:
    """Stable hash function mirroring frontend RAGService.hashString (JS)."""
    h = 0
    for ch in text:
        code = ord(ch)
        h = ((h << 5) - h) + code
        h &= 0xFFFFFFFF  # force 32-bit

    # Interpret as signed 32-bit int, like JS bitwise ops
    if h & 0x80000000:
        h -= 0x100000000
    return h


def _create_embedding(text: str, dimension: int = 384) -> np.ndarray:
    """Create lightweight 384D embedding (same spirit as frontend createQueryEmbedding)."""
    vec = np.zeros(dimension, dtype=float)

    tokens = text.lower().split()
    for idx, token in enumerate(tokens):
        h = _hash_string(token)
        pos = abs(h) % dimension

        # term frequency
        vec[pos] += 1.0

        # simple positional encoding like frontend (1/(idx+1) on next dim)
        pos_weight = 1.0 / (idx + 1)
        vec[(pos + 1) % dimension] += pos_weight

    norm = np.linalg.norm(vec)
    if norm == 0.0:
        return vec
    return vec / norm


def load_corpus() -> None:
    global _faqs, _embeddings_matrix

    if _faqs is not None and _embeddings_matrix is not None:
        return

    faqs_data = _load_json(config.FAQS_PATH)
    _faqs = faqs_data['faqs']

    # Build embeddings directly from (question_fr + answer_fr)
    matrix = []
    for faq in _faqs:
        text = f"{faq['question_fr']} {faq['answer_fr']}"
        emb = _create_embedding(text)
        matrix.append(emb)

    _embeddings_matrix = np.stack(matrix, axis=0)


def retrieve_top_faqs(query: str, language: str = 'fr', top_k: int = 3) -> List[SourceFAQ]:
    load_corpus()
    assert _faqs is not None
    assert _embeddings_matrix is not None

    query_vec = _create_embedding(query)
    q_norm = np.linalg.norm(query_vec)
    if q_norm == 0.0:
        return []

    # cosine similarity: matrix rows are already normalized
    sims = _embeddings_matrix @ (query_vec / q_norm)

    # best indices
    top_indices = np.argsort(-sims)[:top_k]

    results: List[SourceFAQ] = []
    for idx in top_indices:
        similarity = float(sims[idx])
        if similarity < config.MIN_SIMILARITY_WEAK:
            continue

        faq = _faqs[idx]
        results.append(
            SourceFAQ(
                id=faq['id'],
                question_fr=faq['question_fr'],
                answer_fr=faq['answer_fr'],
                question_ar=faq.get('question_ar'),
                answer_ar=faq.get('answer_ar'),
                category=faq.get('category'),
                similarity=similarity,
            )
        )

    return results
