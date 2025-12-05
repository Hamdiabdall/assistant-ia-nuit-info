from __future__ import annotations

from typing import List

import requests

from . import config
from .models import SourceFAQ


class OpenRouterClient:
    def __init__(self) -> None:
        self.api_key = config.OPENROUTER_API_KEY
        self.base_url = config.OPENROUTER_API_BASE.rstrip('/')
        self.model = config.OPENROUTER_MODEL

    def _build_prompt(self, query: str, language: str, faqs: List[SourceFAQ]) -> str:
        # Build a compact context from top-K FAQs
        lines = []
        for idx, faq in enumerate(faqs, start=1):
            q = faq.question_fr
            a = faq.answer_fr
            if language == 'ar':
                q = faq.question_ar or q
                a = faq.answer_ar or a
            lines.append(f"[FAQ {idx}] Q: {q}\nR: {a}")

        context_block = '\n\n'.join(lines) if lines else 'Aucun contexte FAQ fiable.'
        lang_label = 'français' if language == 'fr' else 'arabe'

        prompt = (
            "Tu es un assistant IA low-cost pour la Nuit de l'Info 2025 et les services publics numériques. "
            "Tu dois répondre de manière courte, claire et pédagogique, dans la langue indiquée. "
            "Utilise uniquement les informations ci-dessous comme source principale. Si l'information ne s'y trouve pas, "
            "répond honnêtement que tu n'es pas sûr(e) et propose une réponse prudente. "
            "Répond toujours avec tes propres mots, en reformulant le contexte sans copier mot pour mot les phrases données. "
            "Tu peux ajouter une courte phrase d'explication pour aider l'utilisateur, mais reste concis.\n\n"
            f"Langue de réponse: {lang_label}.\n\n"
            f"Contexte FAQ:\n{context_block}\n\n"
            f"Question utilisateur: {query}\n\n"
            "Réponse:" if language == 'fr' else "الإجابة:"
        )
        return prompt

    def generate(self, query: str, language: str, faqs: List[SourceFAQ]) -> str:
        if not self.api_key:
            # Safety: avoid calling API without key
            raise RuntimeError("OPENROUTER_API_KEY non défini dans l'environnement.")

        prompt = self._build_prompt(query, language, faqs)

        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            # Optional but recommended by OpenRouter:
            "HTTP-Referer": "http://localhost:3000/",
            "X-Title": "NuitInfoAssistant",
        }

        body = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        resp = requests.post(url, json=body, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        # OpenRouter follows OpenAI-like schema
        content = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )

        return content.strip() or "Désolé, je n'ai pas pu générer de réponse pour le moment."


llm_client = OpenRouterClient()
