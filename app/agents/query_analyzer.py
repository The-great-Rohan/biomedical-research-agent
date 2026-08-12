from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.state import ResearchState


class QueryAnalyzer:
    """Analyze a biomedical research question and generate search queries."""

    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=0,
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a biomedical literature search specialist.

Your task is to analyze a biomedical research question and generate
precise PubMed search queries.

The queries should:
- Preserve the scientific meaning of the original question.
- Use appropriate biomedical terminology.
- Include relevant synonyms and abbreviations.
- Avoid unnecessary broadening of the topic.
- Be suitable for PubMed retrieval.
""",
                ),
                (
                    "human",
                    """
Research question:

{question}

Generate a small set of focused PubMed search queries.
Return only the search queries, one query per line.
""",
                ),
            ]
        )

    def analyze(self, state: ResearchState) -> ResearchState:
        """Generate PubMed search queries from the research question."""

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "question": state.question,
            }
        )

        queries: List[str] = [
            line.strip()
            for line in response.content.splitlines()
            if line.strip()
        ]

        state.search_queries = queries

        return state
