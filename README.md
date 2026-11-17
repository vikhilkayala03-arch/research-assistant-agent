# AI-Powered Research Assistant Agent

An AI-powered research assistant built using Python, Streamlit, and Ollama. It accepts research questions, retrieves relevant information from a curated local dataset, generates evidence-based summaries using a locally running LLM, and creates Markdown research reports.

## Features

- Research question processing
- Keyword-based search planning
- Retrieval from a curated local dataset
- AI-powered summarization using Ollama
- Streamlit web dashboard
- Research history
- Markdown report generation
- Downloadable research reports

## Technologies Used

- Python
- Streamlit
- Ollama
- Qwen2.5-Coder 7B
- JSON

## Requirements

- Python 3.10 or above
- Ollama installed
- Qwen2.5-Coder 7B model downloaded

## Setup and Installation

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create a virtual environment:

```powershell
python -m venv .venv
```

4. Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

5. Install the required packages:

```powershell
pip install -r requirements.txt
```

6. Download the Ollama model:

```powershell
ollama pull qwen2.5-coder:7b
```

7. Make sure Ollama is running.

## Run the Application

To start the Streamlit dashboard:

```powershell
streamlit run web_app.py
```

To run the command-line application:

```powershell
python app.py
```

## System Workflow

Research Request → Search Planning → Source Retrieval → Ollama Summarization → Final Research Report

## Dataset

The project uses `dataset/sources.json`, a curated local dataset containing source information, URLs, topics, and evidence notes.

**Note:** This project does not perform live web searches. Its retrieval process uses keyword-based matching against the local dataset.

## Testing

The system was tested using different research questions, including:

- AI applications in healthcare
- AI applications in cybersecurity
- Climate change research
- Ethical AI
- Irrelevant research questions

The testing process evaluates source relevance, summary quality, and the ability to handle questions without relevant dataset sources.

## Limitations

- Search is keyword-based, not semantic search.
- The dataset is limited and locally curated.
- Live web search is not implemented.
- Summary quality depends on the retrieved evidence and local LLM.
- Human verification of sources and generated reports is necessary.

## Project Structure

```text
Research-Assistant-Agent/
├── app.py
├── web_app.py
├── research_agent.py
├── search_engine.py
├── summarizer.py
├── report_generator.py
├── requirements.txt
├── dataset/
│   └── sources.json
├── docs/
├── screenshots/
└── README.md
```

## Project Screenshots

The `screenshots/` folder contains the research testing outputs for the project.

## Author

AI-Powered Research Assistant Agent Project