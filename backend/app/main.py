from __future__ import annotations

from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from . import config
from .models import ChatRequest, ChatResponse, HealthResponse, SourceFAQ
from .rag import load_corpus, retrieve_top_faqs
from .llm_client import llm_client


app = FastAPI(title="Nuit de l'Info Assistant API", version="1.0.0")

# CORS: allow frontend dev origin
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins + ["*"],  # permissive in dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup() -> None:
    # Preload corpus for faster first request
    load_corpus()


@app.get("/api/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/api/chat", response_model=ChatResponse)
async def chat(body: ChatRequest) -> ChatResponse:
    query = body.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query is empty")

    language = body.language or "fr"

    try:
        # RAG: retrieve top FAQs as context
        sources: List[SourceFAQ] = retrieve_top_faqs(query, language=language, top_k=config.MAX_CONTEXT_FAQS)

        max_similarity = max((s.similarity or 0.0) for s in sources) if sources else 0.0

        # Generate answer with OpenRouter LLM
        answer_text = llm_client.generate(query=query, language=language, faqs=sources)

        # Confidence based mainly on retrieval quality
        confidence = max(max_similarity, config.MIN_SIMILARITY_WEAK) if answer_text.strip() else 0.0

        return ChatResponse(
            answer=answer_text,
            sources=sources,
            confidence=float(confidence),
        )

    except HTTPException:
        raise
    except Exception as exc:  # pragma: no cover - generic safety
        # Let frontend fallback to Hybrid mode
        raise HTTPException(status_code=500, detail=str(exc))
