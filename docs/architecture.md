# Architecture

```mermaid
flowchart TD
    A[Research request from user] --> B[Search planning: extract keywords]
    B --> C[Source retrieval: rank curated local dataset]
    C --> D{Relevant sources found?}
    D -- No --> E[Ask user to refine question or add sources]
    D -- Yes --> F[Build evidence prompt with source IDs and URLs]
    F --> G[Gemini LLM summarization]
    G --> H[Generate Markdown research report]
    H --> I[Display report path and sources to user]
    I --> J[Human source verification]
```

## Component responsibilities
- `app.py`: receives the research question and displays results.
- `research_agent.py`: controls the ordered workflow.
- `search_engine.py`: extracts keywords and ranks curated source entries.
- `summarizer.py`: sends retrieved evidence to Gemini and requests a source-grounded synthesis.
- `report_generator.py`: saves the report with source links and a verification warning.
- `dataset/sources.json`: curated source notes and metadata.
