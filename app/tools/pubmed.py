from typing import List

from Bio import Entrez

from app.state import Article


class PubMedTool:
    """Search PubMed and return structured biomedical articles."""

    def __init__(self, email: str):
        self.email = email
        Entrez.email = email

    def search(self, query: str, max_results: int = 10) -> List[Article]:
        """Search PubMed and retrieve article metadata and abstracts."""
        search_handle = Entrez.esearch(
            db="pubmed",
            term=query,
            retmax=max_results,
            sort="relevance",
        )
        search_result = Entrez.read(search_handle)
        search_handle.close()

        pmids = search_result.get("IdList", [])

        if not pmids:
            return []

        fetch_handle = Entrez.efetch(
            db="pubmed",
            id=pmids,
            rettype="medline",
            retmode="xml",
        )
        records = Entrez.read(fetch_handle)
        fetch_handle.close()

        return [
            self._parse_article(record)
            for record in records["PubmedArticle"]
        ]

    @staticmethod
    def _parse_article(record) -> Article:
        """Convert a PubMed XML record into the project Article model."""

        citation = record["MedlineCitation"]
        article = citation["Article"]

        title = str(article.get("ArticleTitle", ""))

        abstract_parts = article.get("Abstract", {}).get(
            "AbstractText", []
        )

        abstract = (
            " ".join(str(part) for part in abstract_parts)
            if abstract_parts
            else None
        )

        authors = []

        for author in article.get("AuthorList", []):
            last_name = author.get("LastName")
            initials = author.get("Initials")

            if last_name:
                authors.append(
                    f"{last_name} {initials or ''}".strip()
                )

        journal = article.get("Journal", {}).get("Title")

        publication_date = None
        journal_issue = article.get("Journal", {}).get(
            "JournalIssue", {}
        )
        pub_date = journal_issue.get("PubDate", {})

        if pub_date:
            publication_date = str(
                pub_date.get("Year")
                or pub_date.get("MedlineDate")
                or ""
            )

        article_ids = record.get("PubmedData", {}).get(
            "ArticleIdList", []
        )

        pmid = str(citation.get("PMID", "")) or None
        doi = None

        for article_id in article_ids:
            if getattr(article_id, "attributes", {}).get(
                "IdType"
            ) == "doi":
                doi = str(article_id)
                break

        return Article(
            title=title,
            authors=authors,
            journal=str(journal) if journal else None,
            publication_date=publication_date,
            pmid=pmid,
            doi=doi,
            abstract=abstract,
        )
