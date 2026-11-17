# Research Assistant Agent

A controlled Python research workflow that accepts a research question, plans keyword searches, retrieves relevant entries from a curated local dataset, asks Gemini to synthesize only the retrieved evidence, and saves a Markdown report.

## Requirements
- Python 3.10+
- Gemini API key from Google AI Studio
- Internet access for Gemini API calls

## Setup (Windows / VS Code)
1. Open this folder in VS Code.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install packages:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env`.
5. Put your newly created API key after `GEMINI_API_KEY=` in `.env`. Never share or upload `.env`.
6. Run:
   ```powershell
   python app.py
   ```

## Workflow
Research request -> search planning -> source retrieval -> evidence-grounded Gemini summarization -> Markdown report.

## Dataset
`dataset/sources.json` is a small curated demonstration corpus with publisher names, source URLs, topic tags, and evidence notes. It is not a live web crawler. Add or update records only after checking the original publisher page.

## Testing
Try these questions:
- How is artificial intelligence used in healthcare and what ethical safeguards are important?
- What are the main cybersecurity practices recommended for individuals?
- What evidence is used to explain climate change?
- How can generative AI affect education and research?

Record whether retrieved sources are relevant, whether every major claim has a source ID, and whether the source page supports the claim. Do not claim that an API test succeeded until you have run it with your own key.

## Limitations
- Retrieval is keyword-based, not semantic search.
- The local corpus is small and does not search the live web.
- A source note may be incomplete or outdated; always open the original URL.
- LLM summaries can omit context or make unsupported statements.
- API availability, quotas, model names, and billing can change.
- Human review is required before submitting or relying on a report.
