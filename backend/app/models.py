from typing import List, Optional
from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str
    language: str = 'fr'
    timestamp: Optional[int] = None


class SourceFAQ(BaseModel):
    id: int
    question_fr: str
    answer_fr: str
    question_ar: Optional[str] = None
    answer_ar: Optional[str] = None
    category: Optional[str] = None
    similarity: Optional[float] = None


class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceFAQ]
    confidence: float


class HealthResponse(BaseModel):
    status: str
