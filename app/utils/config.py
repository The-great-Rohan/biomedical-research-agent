import os

from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NCBI_EMAIL = os.getenv("NCBI_EMAIL")


def validate_config() -> None:
    """Validate required environment variables."""

    missing_variables = []

    if not OPENAI_API_KEY:
        missing_variables.append("OPENAI_API_KEY")

    if not NCBI_EMAIL:
        missing_variables.append("NCBI_EMAIL")

    if missing_variables:
        raise RuntimeError(
            "Missing required environment variables: "
            + ", ".join(missing_variables)
        )
