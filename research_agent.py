"""Controlled research workflow: plan -> retrieve -> summarize -> report."""
from search_engine import retrieve_sources
from summarizer import summarize_with_ollama
from report_generator import save_report

def run_research(question: str) -> dict:
    if not question.strip():
        raise ValueError("Please enter a research question.")

    keywords, sources = retrieve_sources(question)
    if not sources:
        raise RuntimeError(
            "No relevant source found in the curated dataset. Try a related topic "
            "or add trusted sources to dataset/sources.json."
        )
    print("Sending request to Ollama...", flush=True)
    summary = summarize_with_ollama(question, sources)
    print("Ollama response received.", flush=True)
    report_path = save_report(question, keywords, sources, summary)
    return {
        "keywords": keywords,
        "sources": sources,
        "summary": summary,
        "report_path": report_path
    }
