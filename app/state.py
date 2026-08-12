from typing import List, Optional

from pydantic import BaseModel, Field


class Article(BaseModel):
    """Structured representation of a biomedical publication."""

    title: str
    authors: List[str] = Field(default_factory=list)
    journal: Optional[str] = None
    publication_date: Optional[str] = None
    pmid: Optional[str] = None
    doi: Optional[str] = None
    abstract: Optional[str] = None
    relevance_score: Optional[float] = None


class ResearchState(BaseModel):
    """Shared state passed between LangGraph nodes."""

    question: str
    search_queries: List[str] = Field(default_factory=list)
    articles: List[Article] = Field(default_factory=list)
    selected_articles: List[Article] = Field(default_factory=list)
    extracted_evidence: List[str] = Field(default_factory=list)
    final_answer: Optional[str] = None
    citations: List[str] = Field(default_factory=list)
    search_iteration: int = 0
    sufficient_evidence: bool = False
    error: Optional[str] = None
