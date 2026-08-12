from app.graph import build_graph
from app.utils.config import validate_config


def main() -> None:
    """Run the biomedical research agent."""

    validate_config()

    question = input(
        "Enter your biomedical research question:\n> "
    )

    graph = build_graph()

    result = graph.invoke(
        {
            "question": question,
            "search_queries": [],
            "articles": [],
            "selected_articles": [],
            "extracted_evidence": [],
            "citations": [],
            "search_iteration": 0,
            "sufficient_evidence": False,
            "final_answer": None,
            "error": None,
        }
    )

    print("\nGenerated PubMed search queries:\n")

    for index, query in enumerate(
        result.get("search_queries", []),
        start=1,
    ):
        print(f"{index}. {query}")


if __name__ == "__main__":
    main()
