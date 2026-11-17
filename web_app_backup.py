
import streamlit as st
from pathlib import Path
from research_agent import run_research
from datetime import datetime

st.set_page_config(
    page_title="Research Assistant AI",
    page_icon="🔍",
    layout="wide"
)


st.markdown("""
<style>
.stApp {
    background-color: #F8F7F2;
    color: #292929;
}

/* Headings */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #292929 !important;
}

/* Normal text and labels */
.stApp p,
.stApp label,
.stApp li,
.stApp .stMarkdown {
    color: #292929 !important;
}

/* Main title */
.main-title {
    color: #9B762D !important;
    font-size: 42px;
    font-weight: 800;
}

/* Subtitle */
.subtitle {
    color: #555555 !important;
    font-size: 17px;
}


/* Text input */
.stTextArea textarea {
    background-color: #FFFFFF;
    color: #292929;
    border: 1px solid #B18A3B;
    border-radius: 10px;
}

/* Text area placeholder visibility */
.stTextArea textarea::placeholder {
    color: #777777 !important;
    opacity: 1 !important;
}

/* Text entered by user */
.stTextArea textarea {
    color: #292929 !important;
    background-color: #FFFFFF !important;
}

/* Research button text */
div.stButton > button p {
    color: #FFFFFF !important;
    font-weight: bold;
}

/* Research button */
div.stButton > button {
    background-color: #B18A3B;
    color: #FFFFFF !important;
    border-radius: 10px;
    border: none;
    padding: 10px 24px;
    font-weight: bold;
}


/* Research button */
div.stButton > button {
    background-color: #B18A3B;
    color: #FFFFFF !important;
    border-radius: 10px;
    border: none;
    padding: 10px 24px;
    font-weight: bold;
}

/* Download button text visibility */
div.stDownloadButton > button {
    background-color: #292929 !important;
    color: #FFFFFF !important;
}

div.stDownloadButton > button p,
div.stDownloadButton > button span {
    color: #FFFFFF !important;
    visibility: visible !important;
    opacity: 1 !important;
}

/* Expanders */
div[data-testid="stExpander"] {
    background-color: #FFFFFF;
    border: 1px solid #D6C49A;
    border-radius: 10px;
}

/* Success message */
div[data-testid="stAlert"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Initialize Research History
if "research_history" not in st.session_state:
    st.session_state["research_history"] = []
st.markdown(
    '<div class="main-title">🔍 Research Assistant AI</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Your AI-powered research and summarization workspace</div>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("Start Your Research")
question = st.text_area(
    "Enter your research question",
    placeholder="Example: What are the applications of AI in healthcare?",
    height=110
)

if st.button("🚀 Start Research", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a research question.")
    else:
        try:
            with st.spinner("Researching and generating your report..."):
                st.session_state["research_result"] = run_research(question)
            st.success("Research completed successfully!")
            # Save successful research in history
            st.session_state["research_history"].append({
    "question": question,
    "date_time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
    "keywords": st.session_state["research_result"].get("keywords", []),
    "summary": st.session_state["research_result"].get("summary", "")
})
        except Exception as error:
            st.error(f"Research failed: {error}")
            st.session_state.pop("research_result", None)

if "research_result" in st.session_state:
    result = st.session_state["research_result"]

    st.divider()
    st.header("📊 Research Results")

    st.subheader("Search Keywords")
    keywords = result.get("keywords", [])
    st.write(", ".join(map(str, keywords)))

    st.subheader("🤖 AI Summary")
    st.markdown(result.get("summary", "No summary available."))

    st.subheader("📚 Sources Retrieved")
    sources = result.get("sources", [])

    for index, source in enumerate(sources, start=1):
        with st.expander(f"Source {index}"):
            if isinstance(source, dict):
                for key, value in source.items():
                    st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
            else:
                st.write(source)

    report_path = Path(result.get("report_path", ""))

    st.subheader("📄 Research Report")
    if report_path.is_file():
        st.download_button(
            label="⬇️ Download Research Report",
            data=report_path.read_bytes(),
            file_name=report_path.name,
            mime="application/octet-stream"
        )
    else:
        st.info("Report was generated, but its file could not be located.")
# Research History Section
st.divider()
st.header("🕘 Research History")

history = st.session_state.get("research_history", [])

if history:
    if st.button("🗑️ Clear Research History"):
        st.session_state["research_history"] = []
        st.rerun()


if history:
    for index, item in enumerate(reversed(history), start=1):
        with st.expander(f"Research {index}: {item['question']}"):
            st.markdown("**Research Question:**")
            st.write(item["question"])
            st.markdown(f"**Date & Time:** {item.get('date_time', 'Not available')}")
            st.markdown("**Search Keywords:**")
            st.write(", ".join(map(str, item["keywords"])))

            st.markdown("**AI Summary:**")
            st.write(item["summary"])
else:
    st.info("No previous research available yet.")