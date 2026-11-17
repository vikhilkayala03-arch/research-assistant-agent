"""Save a research report as Markdown."""
from datetime import datetime
from pathlib import Path
import re

REPORTS_DIR = Path(__file__).parent / "reports"

def save_report(question: str, keywords: list[str], sources: list[dict], summary: str) -> Path:
    REPORTS_DIR.mkdir(exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", question.lower()).strip("-")[:45] or "research-report"
    path = REPORTS_DIR / f"{datetime.now():%Y%m%d-%H%M%S}-{slug}.md"

    source_list = "\n".join(
        f"- **{s['title']}** — {s['publisher']} ([source]({s['url']})) — ID: `{s['id']}`"
        for s in sources
    ) or "- No matching sources were found in the local dataset."

    content = f"""# Research Assistant Report

**Generated:** {datetime.now():%Y-%m-%d %H:%M}  
**Research question:** {question}

## Search plan
Keywords used: {", ".join(keywords) if keywords else "No keywords extracted"}

## Retrieved sources
{source_list}

## AI-generated synthesis
{summary}

---
*Verification note: This report is an AI-assisted draft based on the listed curated source notes.
Open the original sources and verify claims before academic or professional use.*
"""
    path.write_text(content, encoding="utf-8")
    return path
