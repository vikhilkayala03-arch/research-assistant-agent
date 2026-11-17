
import streamlit as st
from pathlib import Path
from datetime import datetime
from research_agent import run_research

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Research Assistant AI",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION DATA ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: #F7F6F2;
    color: #292929;
}
[data-testid="stHeader"] {
    background: #F7F6F2;
}
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #EEE9DC;
    border-right: 1px solid #D8C79F;
}
[data-testid="stSidebar"] * {
    color: #292929 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 8px;
    border-radius: 9px;
}

/* Hero */
.hero {
    background: linear-gradient(120deg, #FFFFFF, #F0E8D5);
    border: 1px solid #E2D3AE;
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 25px;
}
.hero h1 {
    color: #947027;
    font-size: 38px;
    font-weight: 800;
    margin: 0;
}
.hero p {
    color: #5F5B52;
    font-size: 16px;
    margin-bottom: 0;
}

/* KPI cards */
.kpi {
    background: #FFFFFF;
    border: 1px solid #E5D8B8;
    border-radius: 15px;
    padding: 20px;
    min-height: 115px;
    box-shadow: 0 5px 16px rgba(65,48,15,.05);
}
.kpi-label {
    color: #69645A;
    font-size: 13px;
    font-weight: 600;
}
.kpi-value {
    color: #98742D;
    font-size: 29px;
    font-weight: 800;
    margin-top: 10px;
}

/* Headings */
h1, h2, h3, h4 {
    color: #292929 !important;
}
.stMarkdown p, .stMarkdown li, label {
    color: #343434;
}

/* Text areas */
.stTextArea textarea {
    background: #FFFFFF !important;
    color: #242424 !important;
    -webkit-text-fill-color: #242424 !important;
    border: 1px solid #C7A65C !important;
    border-radius: 12px !important;
}
.stTextArea textarea::placeholder {
    color: #77736B !important;
    -webkit-text-fill-color: #77736B !important;
    opacity: 1 !important;
}
.stTextArea label {
    color: #292929 !important;
    font-weight: 650 !important;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button {
    background: #A98535 !important;
    color: #FFFFFF !important;
    border: 1px solid #A98535 !important;
    border-radius: 10px !important;
    min-height: 44px;
    font-weight: 700 !important;
}
.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover {
    background: #896923 !important;
    color: #FFFFFF !important;
}

/* Expanders and containers */
[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #E1D2AD;
    border-radius: 12px;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border-color: #E5D8B8 !important;
    border-radius: 14px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    color: #49443A;
}
a {
    color: #8A6827 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------------- COMMON FUNCTIONS ----------------
def run_new_research(question):

    if not question.strip():
        st.warning("Please enter a research question.")
        return

    try:
        with st.spinner("Researching and generating your report..."):

            result = run_research(question.strip())

        st.session_state.result = result

        st.session_state.history.append({
            "question": question.strip(),
            "date_time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
            "keywords": result.get("keywords", []),
            "summary": result.get("summary", ""),
            "sources": result.get("sources", []),
            "report_path": str(result.get("report_path", ""))
        })

        st.success("Research completed successfully!")

    except Exception as error:
        st.error(f"Research failed: {error}")


def show_results(result):

    if not result:
        return

    keywords = result.get("keywords", [])
    sources = result.get("sources", [])
    summary = result.get("summary", "")

    st.divider()
    st.header("📊 Research Results")

    tab1, tab2, tab3 = st.tabs([
        "🤖 AI Summary",
        "📚 Sources",
        "📄 Research Report"
    ])

    with tab1:
        st.subheader("AI Generated Summary")
        st.markdown(summary)

        st.subheader("🔑 Search Keywords")
        st.write(", ".join(map(str, keywords)))

    with tab2:
        st.subheader("Sources Retrieved")

        if not sources:
            st.info("No sources retrieved.")
        else:
            for index, source in enumerate(sources, 1):

                with st.expander(f"Source {index}"):

                    if isinstance(source, dict):

                        for key, value in source.items():

                            st.markdown(
                                f"**{key.replace('_', ' ').title()}:** {value}"
                            )

                        url = source.get("url", "")

                        if url and str(url).startswith(("https://", "http://")):
                            st.markdown(f"[Open Original Source]({url})")

                    else:
                        st.write(source)

    with tab3:
        st.subheader("Download Your Research Report")

        report_path = Path(result.get("report_path", ""))

        if report_path.is_file():

            st.download_button(
                "⬇️ Download Research Report",
                data=report_path.read_bytes(),
                file_name=report_path.name,
                mime="application/octet-stream",
                key="main_report_download"
            )
        else:
            st.info("Report file could not be located.")


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown(
        "<div style='text-align:center;font-size:42px;'>📚</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;color:#947027 !important;'>Research Assistant AI</h3>",
        unsafe_allow_html=True
    )

    st.caption("Your intelligent research workspace")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "New Research",
            "Research History",
            "Reports",
            "About"
        ]
    )

    st.divider()
    st.markdown("**Technology Stack**")
    st.caption("Python · Streamlit · Ollama AI")
    st.caption("Curated Research Dataset")


# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🔎 Research Assistant AI</h1>
    <p>Your AI-powered research and summarization workspace</p>
</div>
""", unsafe_allow_html=True)


# =================================================
# DASHBOARD
# =================================================
if page == "Dashboard":

    history = st.session_state.history

    total_research = len(history)

    total_sources = sum(
        len(item["sources"]) for item in history
    )

    total_reports = sum(
        1 for item in history
        if item["report_path"]
        and Path(item["report_path"]).is_file()
    )

    last_research = (
        history[-1]["date_time"] if history else "Not yet"
    )

    st.header("📈 Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("Total Researches", total_research),
        ("Sources Retrieved", total_sources),
        ("Reports Generated", total_reports),
        ("Last Research", last_research)
    ]

    for column, (label, value) in zip(
        [c1, c2, c3, c4], metrics
    ):

        with column:

            st.markdown(f"""
            <div class="kpi">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value" style="font-size:22px;">
                    {value}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    st.header("🔎 Start Your Research")

    with st.form("dashboard_form", clear_on_submit=True):

        question = st.text_area(
            "Enter your research question",
            placeholder="Example: What are the applications of AI in healthcare?",
            height=120
        )

        submitted = st.form_submit_button(
            "🚀 Start Research",
            use_container_width=True
        )

    if submitted:
        run_new_research(question)

    show_results(st.session_state.result)

    st.divider()
    st.header("🕘 Recent Research")

    if history:

        for item in reversed(history[-3:]):

            with st.container(border=True):

                st.write(item["question"])
                st.caption(
                    f"{item['date_time']} · "
                    f"{len(item['sources'])} sources"
                )

    else:
        st.info("Your recent research will appear here.")


# =================================================
# NEW RESEARCH
# =================================================
elif page == "New Research":

    st.header("🔎 New Research")

    with st.form("new_research_form", clear_on_submit=True):

        question = st.text_area(
            "Enter your research question",
            placeholder="Example: How can AI help detect cyber threats?",
            height=130
        )

        submitted = st.form_submit_button(
            "🚀 Generate Research Report",
            use_container_width=True
        )

    if submitted:
        run_new_research(question)

    show_results(st.session_state.result)


# =================================================
# RESEARCH HISTORY
# =================================================
elif page == "Research History":

    st.header("🕘 Research History")

    history = st.session_state.history

    if history:

        st.write(f"Total researches: {len(history)}")

        if st.button("🗑️ Clear Research History"):

            st.session_state.history = []
            st.rerun()

        for index, item in enumerate(reversed(history), 1):

            with st.expander(
                f"Research {index}: {item['question']}"
            ):

                st.markdown("**Research Question**")
                st.write(item["question"])

                st.markdown("**Date & Time**")
                st.write(item["date_time"])

                st.markdown("**Search Keywords**")
                st.write(", ".join(map(str, item["keywords"])))

                st.markdown("**AI Summary**")
                st.markdown(item["summary"])

                st.markdown("**Sources Retrieved**")
                st.write(len(item["sources"]))

                report = Path(item["report_path"]) if item["report_path"] else None

                if report and report.is_file():

                    st.download_button(
                        "⬇️ Download This Report",
                        data=report.read_bytes(),
                        file_name=report.name,
                        key=f"history_download_{index}"
                    )

    else:
        st.info("No previous research available yet.")


# =================================================
# REPORTS
# =================================================
elif page == "Reports":

    st.header("📄 Generated Research Reports")

    reports = [
        item for item in reversed(st.session_state.history)
        if item["report_path"]
        and Path(item["report_path"]).is_file()
    ]

    if reports:

        for index, item in enumerate(reports, 1):

            report = Path(item["report_path"])

            with st.container(border=True):

                st.subheader(f"Report {index}")
                st.write(item["question"])
                st.caption(item["date_time"])

                st.download_button(
                    "⬇️ Download Report",
                    data=report.read_bytes(),
                    file_name=report.name,
                    key=f"report_page_{index}"
                )

    else:
        st.info("No reports generated in this session yet.")


# =================================================
# ABOUT
# =================================================
elif page == "About":

    st.header("ℹ️ About Research Assistant AI")

    st.markdown("""
    ### Project Overview

    Research Assistant AI is an AI-powered research and
    summarization application.

    ### Research Workflow

    1. Research Request
    2. Search Planning
    3. Source Retrieval
    4. AI Summarization
    5. Final Report Generation

    ### Technologies Used

    - Python
    - Streamlit
    - Google Gemini API
    - Curated JSON Dataset

    ### Important Limitation

    This version searches a curated local dataset.
    It does not perform live internet searches.

    Always verify AI-generated information using the
    original source material.
    """)


# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    "<div style='text-align:center;color:#77736B;font-size:12px;'>"
    "Research Assistant AI · AI-powered research workspace"
    "</div>",
    unsafe_allow_html=True
)
