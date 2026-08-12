from typing import List, Optional, TypedDict


class Article(TypedDict, total=False):
    """Structured representation of a biomedical publication."""

    title: str
    authors: List[str]
    journal: Optional[str]
    publication_date: Optional[str]
    pmid: Optional[str]
    doi: Optional[str]
    abstract: Optional[str]
    relevance_score: Optional[float]


class ResearchState(TypedDict, total=False):
    """Shared state passed between LangGraph nodes."""

    question: str
    search_queries: List[str]
    articles: List[Article]
    selected_articles: List[Article]
    extracted_evidence: List[str]
    final_answer: Optional[str]
    citations: List[str]
    search_iteration: int
    sufficient_evidence: bool
    error: Optional[str]
