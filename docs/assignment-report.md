# Build a Research Assistant Agent That Searches and Summarizes Information

## 1. Introduction
Researchers often need to collect information from different sources, organize evidence, and prepare concise summaries. This project demonstrates a controlled AI-assisted workflow that helps with those activities while keeping source links visible for human verification.

## 2. Objective
To build a Python research assistant that accepts a research question, creates a search plan, retrieves relevant entries from a curated local dataset, uses an LLM API to summarize the retrieved evidence, and generates a structured research report.

## 3. Tools and technologies
- Python for workflow implementation.
- Google Gemini API through the official `google-genai` Python SDK for language-model summarization.
- `python-dotenv` for loading the API key from a local environment file.
- JSON for the curated source dataset.
- Markdown for generated reports.

## 4. System workflow
The workflow has five main stages:
1. Research request: the user enters a question.
2. Search planning: the system extracts meaningful keywords.
3. Source retrieval: keyword overlap ranks matching entries in the curated dataset.
4. Summarization: the Gemini model receives the question and retrieved source notes, including source IDs and URLs, and is instructed not to invent unsupported facts.
5. Final report generation: the system saves the synthesis, search terms, and source links in a Markdown report.

See `architecture.md` for the architecture diagram.

## 5. Implementation
The application is divided into modules:
- `app.py`: command-line interface.
- `research_agent.py`: workflow controller.
- `search_engine.py`: search planning and source ranking.
- `summarizer.py`: Gemini API integration.
- `report_generator.py`: Markdown report creation.
- `dataset/sources.json`: curated source collection.

## 6. Sample research questions
The project is designed to test questions about AI in healthcare, cybersecurity practices, climate-change evidence, and generative AI in education. The actual retrieved sources and generated summaries must be captured after running the application with a valid API key.

## 7. Testing and observations
Use `testing-log-template.md` to record actual results. Evaluate source relevance, coverage, traceability, and factual accuracy. Do not report fabricated timings, scores, screenshots, or successful API responses.

## 8. Source verification
The dataset stores the publisher, title, URL, and a short evidence note. The report displays the source links and source IDs. A researcher must open the original pages, check publication context and dates, and confirm that each important statement is supported. The LLM output is a draft, not proof.

## 9. Limitations
- The project searches a small curated local dataset rather than the whole internet.
- Keyword matching can miss relevant sources that use different wording.
- The dataset may become outdated.
- The LLM may omit details or produce unsupported statements despite instructions.
- API usage depends on network access, key permissions, quotas, and model availability.
- Human review is required.

## 10. Lessons learned
Research automation can reduce repetitive searching and drafting, but quality depends on the source collection, retrieval method, prompt design, and verification process. Showing source links improves traceability. Controlled workflows and human review are important for responsible research assistance.

## 11. Conclusion
The project demonstrates an end-to-end research assistant workflow using Python, a curated dataset, an LLM API, and a summarization component. It provides a foundation that can later be extended with an approved live search API, semantic retrieval, and richer report formats.

## 8. Source Verification

The research assistant uses a curated dataset containing information from recognized organizations. The following official sources were checked during source verification:

1. **NIST:** AI Risk Management Framework – https://www.nist.gov/itl/ai-risk-management-framework
2. **FDA:** AI-Enabled Medical Devices – https://www.fda.gov/medical-devices/artificial-intelligence-enabled-medical-devices/list-artificial-intelligence-enabled-medical-devices
3. **NIBIB:** National Institute of Biomedical Imaging and Bioengineering – https://www.nibib.nih.gov/programs/image-processing-visual-perception-and-display
4. **CISA:** AI Cybersecurity Collaboration Playbook – https://www.cisa.gov/sites/default/files/2025-01/JCDC%20AI%20Playbook.pdf
5. **NIST:** Managing Cybersecurity and Privacy Risks in the Age of AI – https://www.nist.gov/blogs/cybersecurity-insights/managing-cybersecurity-and-privacy-risks-age-artificial-intelligence
6. **WHO:** Ethics and Governance of AI for Health – https://www.who.int/Publications/i/item/9789240029200

These sources were checked on their official websites. Source verification helps improve the reliability of the research reports. However, the system still requires manual verification of individual claims.

## 9. Testing and Results

The Research Assistant Agent was tested using three different research questions.

### Test 1: Healthcare
**Research Question:** How is AI used in healthcare?

**Result:** The system retrieved relevant sources related to AI in medical devices, medical imaging and healthcare.

### Test 2: Cybersecurity
**Research Question:** How can AI help in cybersecurity?

**Result:** The improved relevance-based search retrieved cybersecurity-related sources from NIST and CISA.

### Test 3: Unrelated Question
**Research Question:** What are the benefits of online shopping?

**Result:** The system returned zero sources because the curated dataset did not contain relevant information.

### Overall Observation
The tests showed that the system can retrieve relevant information from its curated dataset and generate research summaries using Gemini. The weighted keyword search improved source relevance. However, the system depends on its limited dataset and does not perform live internet searches.

## 10. Lessons Learned

Through this project, I learned:

1. How to build a basic AI research assistant using Python.
2. How to organize research information in a JSON dataset.
3. How keyword-based search planning and relevance scoring work.
4. How to integrate the Gemini API for text summarization.
5. Why source verification is important for reliable research.
6. How to test an AI agent using relevant and unrelated questions.
7. The limitations of curated datasets and AI-generated summaries.

## 11. Conclusion

The Research Assistant Agent demonstrates how AI can automate basic research tasks. It accepts a research question, identifies keywords, retrieves relevant information from a curated dataset, generates a summary using Gemini, and saves a final report.

The project provides a foundation for research automation. Future improvements could include live web search, a larger verified dataset, and more advanced semantic search.

