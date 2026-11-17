"""Command-line entry point for the Research Assistant Agent."""
from research_agent import run_research

def main():
    print("=" * 64)
    print("             RESEARCH ASSISTANT AGENT")
    print("=" * 64)
    print("Ask a research question. Example:")
    print("How is artificial intelligence used in healthcare?")
    question = input("\nResearch question: ").strip()

    try:
        result = run_research(question)
        print("\nSEARCH PLAN")
        print(", ".join(result["keywords"]) or "No keywords")
        print("\nRETRIEVED SOURCES")
        for source in result["sources"]:
            print(f"- {source['title']} ({source['publisher']})")
            print(f"  {source['url']}")
        print("\nRESEARCH SUMMARY")
        print(result["summary"])
        print(f"\nReport saved to: {result['report_path']}")
    except Exception as exc:
        print(f"\nCould not complete the research: {exc}")
        print("Check your .env API key, internet connection, and dataset.")

if __name__ == "__main__":
    main()
