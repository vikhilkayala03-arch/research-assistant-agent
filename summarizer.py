
"""Local AI summarization using Ollama."""
import json
import urllib.request
import urllib.error


def summarize_with_ollama(question: str, sources: list[dict]) -> str:
    model = "qwen2.5-coder:7b"
    url = "http://localhost:11434/api/generate"

    source_text = "\n\n".join(
        f"Source ID: {s['id']}\n"
        f"Title: {s['title']}\n"
        f"Publisher: {s['publisher']}\n"
        f"URL: {s['url']}\n"
        f"Evidence notes: {s['content']}"
        for s in sources
    )

    prompt = f"""
You are a careful research assistant. Answer using only the
source notes below. Do not invent facts, statistics, quotations,
or references. If evidence is insufficient, say so clearly.
Include inline source IDs such as [WHO-AI-HEALTH].

Research question: {question}

Retrieved source notes:
{source_text}

Write a concise report with:
1. Research question
2. Executive summary
3. Key findings (with source IDs)
4. Limitations / evidence gaps
5. Conclusion
6. Sources (title, publisher, URL)
"""

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            result = json.loads(response.read().decode("utf-8"))

        answer = result.get("response", "").strip()

        if not answer:
            raise RuntimeError("Ollama returned an empty response.")

        return answer

    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not connect to Ollama. Make sure Ollama is running."
        ) from error
