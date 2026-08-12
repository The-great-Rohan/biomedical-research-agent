# Biomedical Research Agent

An agentic biomedical literature research system built with LangGraph and LangChain.

## Overview

Biomedical research increasingly requires researchers to search, evaluate, and synthesize large amounts of scientific literature. This project aims to develop an agentic research assistant that can perform these tasks through a structured, tool-using workflow.

The system is designed to accept a biomedical research question, retrieve relevant scientific literature, assess the retrieved evidence, extract key information, and generate a citation-aware scientific synthesis.

Unlike a conventional question-answering system, the proposed architecture uses an explicit agent workflow that can make decisions about which tools to use, evaluate intermediate results, and repeat research steps when the available evidence is insufficient.

## Architecture

The planned research workflow is:

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
