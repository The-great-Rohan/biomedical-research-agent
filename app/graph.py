from langgraph.graph import END, START, StateGraph

from app.agents.query_analyzer import QueryAnalyzer
from app.state import ResearchState


query_analyzer = QueryAnalyzer()


def analyze_query(state: ResearchState) -> dict:
    """Analyze the research question and generate PubMed queries."""

    return query_analyzer.analyze(state)


def build_graph():
    """Build the biomedical research workflow."""

    workflow = StateGraph(ResearchState)

    workflow.add_node("analyze_query", analyze_query)

    workflow.add_edge(START, "analyze_query")
    workflow.add_edge("analyze_query", END)

    return workflow.compile()
