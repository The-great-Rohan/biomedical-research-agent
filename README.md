# Biomedical Research Agent

An agentic biomedical literature research system built with LangGraph and LangChain.

## Project Status

Early-stage development. The system is designed as a research assistant for biomedical literature retrieval, evidence extraction, scientific synthesis, and citation verification.

## Objectives

The system will accept a scientific question and execute a structured research workflow rather than returning a single unconstrained LLM response.

## Planned Workflow

```text
User Question
      |
      v
Query Analysis
      |
      v
PubMed Search
      |
      v
Article Retrieval
      |
      v
Relevance Assessment
      |
      v
Evidence Extraction
      |
      v
Scientific Synthesis
      |
      v
Citation Verification
      |
      v
Final Answer



The workflow will be implemented as a stateful graph using LangGraph, allowing the system to make conditional decisions and repeat research steps when the retrieved evidence is insufficient.

Core Features
Biomedical literature retrieval through PubMed
Scientific query analysis
Article relevance assessment
Evidence extraction
Citation-aware synthesis
Conditional agent workflows
Structured agent state
Error handling and retry mechanisms
Evaluation of retrieval and citation quality
Technology Stack
Python
LangChain
LangGraph
NCBI Entrez / PubMed API
Pydantic
Large Language Models
Git and GitHub
Research Domain

The initial implementation will focus on biomedical and infectious disease research.

Example research areas include:

Virology
EBV and transplantation
HPV
Infectious diseases
Molecular epidemiology
Host-pathogen interactions
Project Goals

The main goal is to develop a reproducible and extensible agentic workflow for biomedical literature research.

The project will emphasize:

Reliable literature retrieval
Structured evidence extraction
Citation accuracy
Transparent agent workflows
Reproducible evaluation
Roadmap
Phase 1: Core Research Workflow
 Define agent state
 Implement PubMed search tool
 Implement query analysis
 Implement article retrieval
 Implement relevance assessment
 Implement evidence extraction
 Implement scientific synthesis
 Implement citation verification
Phase 2: Agentic Workflow
 Implement LangGraph state management
 Add conditional routing
 Add iterative literature search
 Add error handling and retries
 Add structured outputs
Phase 3: Evaluation
 Create biomedical benchmark questions
 Add unit tests
 Evaluate retrieval performance
 Evaluate citation accuracy
 Evaluate answer consistency
 Document limitations and failure cases
Phase 4: Biomedical Demonstration
 Develop EBV and transplantation research examples
 Develop virology literature search examples
 Compare agent-generated results with manually curated evidence
Project Status

This project is currently under active development.

The initial version focuses on establishing the core LangGraph workflow and reliable PubMed retrieval before adding more advanced agentic capabilities.

Disclaimer

This project is a research and software engineering prototype. It is not intended to provide clinical diagnosis, treatment recommendations, or medical advice.

Author

S. Alavi
