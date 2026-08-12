from app.agents.query_analyzer import QueryAnalyzer
from app.state import ResearchState
from app.utils.config import validate_config


def main() -> None:
    """Run a basic biomedical research query analysis."""

    validate_config()

    question = input("Enter your biomedical research question:\n> ")

    state = ResearchState(question=question)

    analyzer = QueryAnalyzer()
    state = analyzer.analyze(state)

    print("\nGenerated PubMed search queries:\n")

    for index, query in enumerate(state.search_queries, start=1):
        print(f"{index}. {query}")


if __name__ == "__main__":
    main()
