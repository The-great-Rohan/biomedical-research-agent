# Biomedical Research Agent

An agentic biomedical literature research system built with LangGraph and LangChain.

## Overview

Biomedical research increasingly requires researchers to search, evaluate, and synthesize large amounts of scientific literature. This project aims to develop an agentic research assistant that can perform these tasks through a structured, tool-using workflow.

The system is designed to accept a biomedical research question, retrieve relevant scientific literature, assess the retrieved evidence, extract key information, and generate a citation-aware scientific synthesis.

Unlike a conventional question-answering system, the proposed architecture uses an explicit agent workflow that can make decisions about which tools to use, evaluate intermediate results, and repeat research steps when the available evidence is insufficient.

## Architecture

The planned research workflow is:

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

The workflow will be implemented as a stateful graph using LangGraph. Each stage will operate on a shared research state, allowing the system to make conditional decisions and perform iterative searches when necessary.

## Core Features

- Biomedical literature retrieval through PubMed
- Scientific query analysis
- Article relevance assessment
- Evidence extraction from scientific literature
- Citation-aware scientific synthesis
- Conditional agent workflows
- Stateful research processes
- Structured outputs using Pydantic
- Error handling and retry mechanisms
- Evaluation of retrieval and citation quality

## Technology Stack

- Python
- LangChain
- LangGraph
- NCBI Entrez / PubMed API
- Pydantic
- Large Language Models
- Git and GitHub

## Research Domain

The initial implementation will focus on biomedical and infectious disease research.

Example research areas include:

- Virology
- EBV and transplantation
- HPV
- Infectious diseases
- Molecular epidemiology
- Host-pathogen interactions

The system is designed to remain domain-independent at the architectural level while providing biomedical examples for evaluation and demonstration.

## Project Goals

The primary goal is to develop a reproducible and extensible agentic workflow for biomedical literature research.

The project will focus on:

- Reliable scientific literature retrieval
- Structured evidence extraction
- Citation accuracy
- Transparent agent workflows
- Reproducible evaluation
- Robust handling of incomplete or insufficient evidence

## Agent Workflow

The research agent will be designed around several functional components.

### Query Analyzer

The query analyzer will interpret the user's research question and identify the information required to answer it.

### Literature Researcher

The research component will interact with PubMed and retrieve potentially relevant scientific articles.

### Relevance Evaluator

Retrieved articles will be assessed for their relevance to the research question before being used for evidence synthesis.

### Evidence Extractor

Relevant publications will be processed to extract structured information such as study population, study design, biological targets, major findings, and relevant conclusions.

### Scientific Synthesizer

The synthesizer will combine extracted evidence into a structured scientific response while preserving the connection between claims and their supporting sources.

### Citation Verifier

The citation verification component will check whether generated claims are supported by the retrieved literature.

## LangGraph Design

LangGraph will be used to coordinate the research workflow through explicit states and conditional transitions.

A simplified version of the planned graph is:

START
  |
  v
Analyze Query
  |
  v
Search PubMed
  |
  v
Retrieve Articles
  |
  v
Evaluate Relevance
  |
  v
Sufficient Evidence?
   /          \
 NO            YES
 |              |
 v              v
Search Again   Extract Evidence
 |              |
 └───────>──────┘
                |
                v
          Scientific Synthesis
                |
                v
         Citation Verification
                |
                v
               END

This architecture allows the agent to perform iterative research rather than relying on a single retrieval step.

## Roadmap

### Phase 1: Core Research Workflow

- [ ] Define agent state
- [ ] Implement PubMed search tool
- [ ] Implement query analysis
- [ ] Implement article retrieval
- [ ] Implement relevance assessment
- [ ] Implement evidence extraction
- [ ] Implement scientific synthesis
- [ ] Implement citation verification

### Phase 2: Agentic Workflow

- [ ] Implement LangGraph state management
- [ ] Add conditional routing
- [ ] Add iterative literature search
- [ ] Add error handling and retries
- [ ] Add structured outputs
- [ ] Add research state persistence

### Phase 3: Evaluation

- [ ] Create representative biomedical research questions
- [ ] Build a small evaluation dataset
- [ ] Add unit tests for research tools
- [ ] Evaluate retrieval quality
- [ ] Evaluate citation accuracy
- [ ] Evaluate answer consistency
- [ ] Document failure cases and limitations

### Phase 4: Biomedical Demonstration

- [ ] Develop EBV and transplantation research examples
- [ ] Develop virology literature search examples
- [ ] Develop infectious disease research examples
- [ ] Compare agent-generated results with manually curated evidence
- [ ] Document representative research workflows

## Example Research Questions

The system will eventually be evaluated using questions such as:

What are the recent studies evaluating EBV viral load and PTLD risk in solid organ transplant recipients?

What EBV-associated microRNAs have been investigated as biomarkers in transplant recipients?

What are the recent molecular epidemiological findings regarding high-risk HPV genotypes?

The examples will be used to evaluate retrieval, evidence extraction, synthesis, and citation accuracy.

## Project Status

This project is currently under active development.

The initial implementation focuses on establishing the core LangGraph workflow and reliable PubMed retrieval before introducing more advanced agentic capabilities.

## Future Development

Future versions may include:

- Full-text article retrieval
- Retrieval-augmented generation
- Vector-based semantic search
- PDF processing
- Multi-agent research workflows
- Literature comparison and evidence tables
- Automated reference management
- Research report generation
- Integration with additional biomedical databases

## Disclaimer

This project is a research and software engineering prototype. It is not intended to provide clinical diagnosis, treatment recommendations, or medical advice.

## Author

S. Alavi
