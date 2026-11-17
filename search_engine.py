
"""Search planning and relevance-based retrieval over curated sources."""
import json
import re
from pathlib import Path

DATA_PATH = Path(__file__).parent / "dataset" / "sources.json"

STOP_WORDS = {
    "the", "and", "for", "with", "from", "that", "this", "what",
    "how", "are", "was", "were", "into", "about", "does", "can",
    "use", "using", "its", "their", "your", "our", "who", "why",
    "when", "where", "help", "used", "artificial", "intelligence"
}

def plan_search(question: str) -> list[str]:
    """Create a simple keyword plan."""
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9-]*", question.lower())
    return list(dict.fromkeys(
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    ))

def load_sources() -> list[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def retrieve_sources(question: str, limit: int = 5):
    """Rank sources by topic, title and content relevance."""
    keywords = plan_search(question)
    ranked = []

    for source in load_sources():
        title = source.get("title", "").lower()
        topics = [topic.lower() for topic in source.get("topics", [])]
        content = source.get("content", "").lower()

        score = 0

        for keyword in keywords:
            if keyword in topics:
                score += 5
            if re.search(r"\b" + re.escape(keyword) + r"\b", title):
                score += 3
            if re.search(r"\b" + re.escape(keyword) + r"\b", content):
                score += 1

        if score >= 3:
            ranked.append((score, source))

    ranked.sort(key=lambda item: item[0], reverse=True)

    return keywords, [source for score, source in ranked[:limit]]
