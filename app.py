# import streamlit as st
# import time
# from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="AI Research Pipeline",
#     page_icon="🔬",
#     layout="wide",
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Syne', sans-serif;
# }

# /* Dark background */
# .stApp {
#     background-color: #0d0d0f;
#     color: #e8e6e1;
# }

# /* Hide default streamlit chrome */
# #MainMenu, footer, header { visibility: hidden; }

# /* Title */
# .pipeline-title {
#     font-family: 'Syne', sans-serif;
#     font-weight: 800;
#     font-size: 2.8rem;
#     letter-spacing: -1px;
#     color: #f0ece4;
#     margin-bottom: 0;
# }
# .pipeline-sub {
#     font-family: 'Space Mono', monospace;
#     font-size: 0.75rem;
#     color: #6b6860;
#     letter-spacing: 3px;
#     text-transform: uppercase;
#     margin-top: 0.2rem;
#     margin-bottom: 2rem;
# }

# /* Step card */
# .step-card {
#     background: #16161a;
#     border: 1px solid #2a2a30;
#     border-left: 3px solid #c8ff6e;
#     border-radius: 6px;
#     padding: 1.1rem 1.4rem;
#     margin-bottom: 0.8rem;
#     font-family: 'Space Mono', monospace;
#     font-size: 0.82rem;
#     color: #c0bdb7;
#     position: relative;
# }
# .step-card.active {
#     border-left-color: #ff9f43;
#     background: #1a1714;
#     animation: pulse-border 1.4s ease-in-out infinite;
# }
# .step-card.done {
#     border-left-color: #c8ff6e;
#     opacity: 0.85;
# }
# .step-card.pending {
#     border-left-color: #2a2a30;
#     opacity: 0.45;
# }

# @keyframes pulse-border {
#     0%, 100% { border-left-color: #ff9f43; }
#     50% { border-left-color: #ffd700; }
# }

# .step-label {
#     font-size: 0.65rem;
#     letter-spacing: 2.5px;
#     text-transform: uppercase;
#     margin-bottom: 0.25rem;
# }
# .step-label.active { color: #ff9f43; }
# .step-label.done   { color: #c8ff6e; }
# .step-label.pending{ color: #444; }

# .step-title {
#     font-family: 'Syne', sans-serif;
#     font-weight: 600;
#     font-size: 1rem;
#     color: #f0ece4;
# }
# .step-status-icon {
#     position: absolute;
#     right: 1.2rem;
#     top: 50%;
#     transform: translateY(-50%);
#     font-size: 1.1rem;
# }

# /* Result boxes */
# .result-box {
#     background: #16161a;
#     border: 1px solid #2a2a30;
#     border-radius: 6px;
#     padding: 1.3rem 1.5rem;
#     font-family: 'Space Mono', monospace;
#     font-size: 0.8rem;
#     color: #c8c5be;
#     white-space: pre-wrap;
#     line-height: 1.7;
#     max-height: 340px;
#     overflow-y: auto;
# }
# .result-box::-webkit-scrollbar { width: 5px; }
# .result-box::-webkit-scrollbar-track { background: #0d0d0f; }
# .result-box::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }

# .section-label {
#     font-family: 'Space Mono', monospace;
#     font-size: 0.65rem;
#     letter-spacing: 3px;
#     text-transform: uppercase;
#     color: #6b6860;
#     margin-bottom: 0.5rem;
# }

# /* Report card */
# .report-card {
#     background: #13150f;
#     border: 1px solid #c8ff6e33;
#     border-top: 3px solid #c8ff6e;
#     border-radius: 6px;
#     padding: 1.6rem 1.8rem;
#     color: #ddd9d1;
#     line-height: 1.8;
#     white-space: pre-wrap;
# }

# /* Critic card */
# .critic-card {
#     background: #150f13;
#     border: 1px solid #ff6eb433;
#     border-top: 3px solid #ff6eb4;
#     border-radius: 6px;
#     padding: 1.6rem 1.8rem;
#     color: #ddd9d1;
#     font-family: 'Space Mono', monospace;
#     font-size: 0.8rem;
#     line-height: 1.8;
#     white-space: pre-wrap;
# }

# /* Query input area */
# .stTextInput > div > div > input {
#     background: #16161a !important;
#     border: 1px solid #2a2a30 !important;
#     border-radius: 4px !important;
#     color: #f0ece4 !important;
#     font-family: 'Space Mono', monospace !important;
#     font-size: 0.9rem !important;
#     padding: 0.7rem 1rem !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: #c8ff6e !important;
#     box-shadow: 0 0 0 1px #c8ff6e40 !important;
# }

# /* Button */
# .stButton > button {
#     background: #c8ff6e !important;
#     color: #0d0d0f !important;
#     font-family: 'Space Mono', monospace !important;
#     font-weight: 700 !important;
#     font-size: 0.8rem !important;
#     letter-spacing: 1.5px !important;
#     text-transform: uppercase !important;
#     border: none !important;
#     border-radius: 3px !important;
#     padding: 0.55rem 1.8rem !important;
#     transition: opacity 0.2s !important;
# }
# .stButton > button:hover { opacity: 0.85 !important; }

# /* Divider */
# hr { border-color: #1e1e24 !important; }
# </style>
# """, unsafe_allow_html=True)


# # ── Header ────────────────────────────────────────────────────────────────────
# st.markdown('<div class="pipeline-title">Research Pipeline</div>', unsafe_allow_html=True)
# st.markdown('<div class="pipeline-sub">Autonomous · Multi-Agent · Agentic</div>', unsafe_allow_html=True)

# # ── Input ─────────────────────────────────────────────────────────────────────
# col_input, col_btn = st.columns([5, 1])
# with col_input:
#     topic = st.text_input("", placeholder="Enter a research topic…", label_visibility="collapsed")
# with col_btn:
#     run = st.button("Run →")

# st.markdown("---")

# # ── Pipeline steps definition ─────────────────────────────────────────────────
# STEPS = [
#     {"id": 1, "title": "Web Search Agent",    "desc": "Finds recent & reliable sources on your topic"},
#     {"id": 2, "title": "Reader / Scraper Agent","desc": "Picks top URLs and extracts deep content"},
#     {"id": 3, "title": "Writer Chain",         "desc": "Drafts a structured research report"},
#     {"id": 4, "title": "Critic Chain",         "desc": "Evaluates and scores the final report"},
# ]

# def render_steps(current_step: int):
#     """Render the 4 step tracker cards."""
#     for s in STEPS:
#         sid = s["id"]
#         if sid < current_step:
#             status, icon = "done",    "✓"
#         elif sid == current_step:
#             status, icon = "active",  "⟳"
#         else:
#             status, icon = "pending", "·"

#         st.markdown(f"""
#         <div class="step-card {status}">
#             <div class="step-label {status}">Step {sid}</div>
#             <div class="step-title">{s['title']}</div>
#             <div style="font-size:0.72rem;color:#555;margin-top:2px">{s['desc']}</div>
#             <span class="step-status-icon">{icon}</span>
#         </div>
#         """, unsafe_allow_html=True)


# # ── Main pipeline execution ───────────────────────────────────────────────────
# if run and topic.strip():

#     left, right = st.columns([1, 1.8], gap="large")

#     with left:
#         st.markdown('<div class="section-label">Pipeline Progress</div>', unsafe_allow_html=True)
#         step_placeholder = st.empty()

#     with right:
#         results_placeholder = st.empty()

#     state = {}

#     # ---------- STEP 1 ----------
#     with step_placeholder.container():
#         render_steps(1)

#     with results_placeholder.container():
#         st.markdown('<div class="section-label">Step 1 — Search Agent</div>', unsafe_allow_html=True)
#         with st.spinner("Searching the web…"):
#             search_agent = build_search_agent()
#             search_result = search_agent.invoke({
#                 "messages": [("user",
#                     f"find recent and reliable information on the topic: {topic} "
#                     f"using web search tool and return the info in structured format")]
#             })
#         state["search_results"] = search_result["messages"][-1].content
#         st.markdown(f'<div class="result-box">{state["search_results"]}</div>', unsafe_allow_html=True)

#     # ---------- STEP 2 ----------
#     with step_placeholder.container():
#         render_steps(2)

#     with results_placeholder.container():
#         st.markdown('<div class="section-label">Step 2 — Reader / Scraper Agent</div>', unsafe_allow_html=True)
#         with st.spinner("Scraping top resource…"):
#             reader_agent = build_reader_agent()
#             reader_results = reader_agent.invoke({
#                 "messages": [(
#                     "user",
#                     f"Based on the following search results about '{topic}',"
#                     f"pick the most relevant URL and scrape it for deeper content.\n\n"
#                     f"Search Results:\n{state['search_results'][:800]}"
#                 )]
#             })
#         state["scraped_content"] = reader_results["messages"][-1].content
#         st.markdown(f'<div class="result-box">{state["scraped_content"]}</div>', unsafe_allow_html=True)

#     # ---------- STEP 3 ----------
#     with step_placeholder.container():
#         render_steps(3)

#     with results_placeholder.container():
#         st.markdown('<div class="section-label">Step 3 — Writer Chain</div>', unsafe_allow_html=True)
#         with st.spinner("Drafting report…"):
#             combined = (
#                 f"SEARCH RESULTS:\n{state['search_results']}\n\n"
#                 f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}\n\n"
#             )
#             state["report"] = writer_chain.invoke({"topic": topic, "research": combined})
#         st.markdown(f'<div class="report-card">{state["report"]}</div>', unsafe_allow_html=True)

#     # ---------- STEP 4 ----------
#     with step_placeholder.container():
#         render_steps(4)

#     with results_placeholder.container():
#         st.markdown('<div class="section-label">Step 4 — Critic Chain</div>', unsafe_allow_html=True)
#         with st.spinner("Evaluating report…"):
#             state["feedback"] = critic_chain.invoke({"report": state["report"]})
#         st.markdown(f'<div class="critic-card">{state["feedback"]}</div>', unsafe_allow_html=True)

#     # ---------- ALL DONE ----------
#     with step_placeholder.container():
#         render_steps(5)  # all steps marked done

#     st.success("✓ Pipeline complete")

#     # Download button for the report
#     st.download_button(
#         label="Download Report",
#         data=state["report"],
#         file_name=f"research_{topic[:30].replace(' ','_')}.txt",
#         mime="text/plain",
#     )

# elif run and not topic.strip():
#     st.warning("Please enter a research topic first.")



print("\n"+"="*50)
# =============================================================================
# Research Pipeline – Streamlit Frontend
# =============================================================================
# How to run:
#   streamlit run App.py
#
# Required dependencies (see requirements.txt):
#   streamlit, requests, beautifulsoup4, lxml, langchain, plus project modules:
#   agents.py, pipeline.py, tools.py
#
# NOTE: Steps are executed one-by-one so the UI updates live after each step.
#       We call the same agents/chains that pipeline.py uses internally.
# =============================================================================

import traceback
import streamlit as st
from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# MAX_TOPIC_LENGTH = 300

# STEPS = [
#     {"key": "search_results",  "label": "Web Search",       "icon": "🔍"},
#     {"key": "scraped_content", "label": "Reader / Scraper",  "icon": "📄"},
#     {"key": "report",          "label": "Writer",            "icon": "✍️"},
#     {"key": "feedback",        "label": "Critic",            "icon": "🧐"},
# ]

# RESULT_META = [
#     {"key": "search_results",  "title": "Web Search Results", "icon": "🔍"},
#     {"key": "scraped_content", "title": "Scraped Content",    "icon": "📄"},
#     {"key": "report",          "title": "Final Report",       "icon": "✍️"},
#     {"key": "feedback",        "title": "Critic Feedback",    "icon": "🧐"},
# ]

# # ---------------------------------------------------------------------------
# # CSS
# # ---------------------------------------------------------------------------

# CUSTOM_CSS = """
# <style>
# [data-testid="stAppViewContainer"] { background: #f7f8fc; }
# [data-testid="stSidebar"] { display: none; }

# .step-card {
#     border-radius: 12px;
#     padding: 14px 10px;
#     text-align: center;
#     font-size: 0.82rem;
#     font-weight: 600;
#     border: 2px solid transparent;
#     transition: all 0.25s ease;
#     margin-bottom: 4px;
# }
# .step-pending { background: #e9ecef; color: #868e96; border-color: #dee2e6; }
# .step-active  { background: #fff3cd; color: #856404; border-color: #ffc107;
#                 box-shadow: 0 0 0 3px rgba(255,193,7,0.25); }
# .step-done    { background: #d1e7dd; color: #0a3622; border-color: #86c9a4; }

# .result-box {
#     background: #ffffff;
#     border: 1px solid #dee2e6;
#     border-radius: 10px;
#     padding: 16px 18px;
#     font-family: 'Courier New', Courier, monospace;
#     font-size: 0.82rem;
#     line-height: 1.6;
#     min-height: 340px;
#     max-height: 340px;
#     overflow-y: auto;
#     white-space: pre-wrap;
#     word-break: break-word;
#     color: #212529;
#     margin-bottom: 12px;
# }
# .result-box-done {
#     border-color: #86c9a4 !important;
#     border-width: 2px !important;
# }
# .result-running {
#     color: #856404 !important;
#     font-style: italic;
#     font-family: sans-serif !important;
#     background: #fff3cd !important;
#     border-color: #ffc107 !important;
#     border-width: 2px !important;
#     display: flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     font-size: 0.95rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.02em;
# }
# .result-empty {
#     color: #adb5bd;
#     font-style: italic;
#     font-family: sans-serif;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     height: 100%;
# }
# .section-title {
#     font-size: 1rem;
#     font-weight: 700;
#     color: #343a40;
#     margin-bottom: 6px;
# }
# div[data-testid="stButton"] > button {
#     background: #4361ee; color: #fff; border: none;
#     border-radius: 8px; padding: 0.55rem 2rem;
#     font-size: 1rem; font-weight: 600; width: 100%;
#     transition: background 0.2s;
# }
# div[data-testid="stButton"] > button:hover { background: #3251d3; }
# div[data-testid="stDownloadButton"] > button {
#     background: #2dc653; color: #fff; border: none;
#     border-radius: 8px; padding: 0.5rem 1.6rem;
#     font-weight: 600; transition: background 0.2s;
# }
# div[data-testid="stDownloadButton"] > button:hover { background: #24a845; }
# </style>
# """

# # ---------------------------------------------------------------------------
# # Session-state helpers
# # ---------------------------------------------------------------------------

# def init_session_state() -> None:
#     """Initialise required session-state keys on first load."""
#     defaults: dict = {
#         "topic": "",
#         "pipeline_state": {},   # accumulates results key-by-key as steps finish
#         "active_step": -1,      # index of step currently running (-1 = idle)
#         "running": False,
#         "error": None,
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value


# # ---------------------------------------------------------------------------
# # Validation
# # ---------------------------------------------------------------------------

# def validate_topic(topic: str) -> str | None:
#     """Return an error string if the topic is invalid, else None."""
#     stripped = topic.strip()
#     if not stripped:
#         return "Please enter a research topic before running."
#     if len(stripped) > MAX_TOPIC_LENGTH:
#         return f"Topic is too long (max {MAX_TOPIC_LENGTH} characters)."
#     return None


# # ---------------------------------------------------------------------------
# # Individual step runners
# # ---------------------------------------------------------------------------

# def run_step_search(topic: str) -> str:
#     """Step 1 – run the search agent and return its output string."""
#     agent = build_search_agent()
#     result = agent.invoke({
#         "messages": [(
#             "user",
#             f"Find recent and reliable information on the topic: {topic} "
#             "using the web search tool and return the info in structured format."
#         )]
#     })
#     return result["messages"][-1].content


# def run_step_reader(topic: str, search_results: str) -> str:
#     """Step 2 – run the reader/scraper agent and return its output string."""
#     agent = build_reader_agent()
#     result = agent.invoke({
#         "messages": [(
#             "user",
#             f"Based on the following search results about '{topic}', "
#             "pick the most relevant URL and scrape it for deeper content.\n\n"
#             f"Search Results:\n{search_results[:800]}"
#         )]
#     })
#     return result["messages"][-1].content


# def run_step_writer(topic: str, search_results: str, scraped_content: str) -> str:
#     """Step 3 – run the writer chain and return the report string."""
#     combined = (
#         f"SEARCH RESULTS:\n{search_results}\n\n"
#         f"DETAILED SCRAPED CONTENT:\n{scraped_content}\n\n"
#     )
#     return writer_chain.invoke({"topic": topic, "research": combined})


# def run_step_critic(report: str) -> str:
#     """Step 4 – run the critic chain and return the feedback string."""
#     return critic_chain.invoke({"report": report})


# # ---------------------------------------------------------------------------
# # Live pipeline executor
# # ---------------------------------------------------------------------------

# def execute_pipeline_live(
#     topic: str,
#     tracker_placeholder: st.delta_generator.DeltaGenerator,
#     results_placeholder: st.delta_generator.DeltaGenerator,
# ) -> None:
#     """
#     Run all four pipeline steps sequentially.
#     After each step completes, immediately re-render the tracker (green card)
#     and result boxes (with content) so the user sees progress live.
#     """
#     state: dict = {}
#     st.session_state.pipeline_state = {}
#     st.session_state.error = None

#     def step_fn_search():
#         return run_step_search(topic)

#     def step_fn_reader():
#         return run_step_reader(topic, state["search_results"])

#     def step_fn_writer():
#         return run_step_writer(topic, state["search_results"], state["scraped_content"])

#     def step_fn_critic():
#         return run_step_critic(state["report"])

#     step_functions = [step_fn_search, step_fn_reader, step_fn_writer, step_fn_critic]

#     for step_index, (step_meta, step_fn) in enumerate(zip(STEPS, step_functions)):
#         st.session_state.active_step = step_index

#         # Mark current step yellow in tracker
#         with tracker_placeholder.container():
#             render_step_tracker(state, step_index)

#         # Show ⏳ running state inside the active result box
#         with results_placeholder.container():
#             render_all_result_boxes(state, active_step=step_index)

#         try:
#             output = step_fn()
#         except Exception as exc:
#             st.session_state.error = str(exc)
#             st.session_state.active_step = -1
#             traceback.print_exc()
#             return

#         # Store result and update session state
#         state[step_meta["key"]] = output
#         st.session_state.pipeline_state = dict(state)

#         # Mark completed step green in tracker
#         with tracker_placeholder.container():
#             render_step_tracker(state, step_index + 1)

#         # Show result box for this step immediately (and all prior ones)
#         with results_placeholder.container():
#             render_all_result_boxes(state)

#     st.session_state.active_step = len(STEPS)  # all done


# # ---------------------------------------------------------------------------
# # UI rendering helpers
# # ---------------------------------------------------------------------------

# def render_step_tracker(pipeline_state: dict, active_step: int) -> None:
#     """Render the 4-step progress tracker as colour-coded cards."""
#     cols = st.columns(len(STEPS))
#     for idx, (step, col) in enumerate(zip(STEPS, cols)):
#         if step["key"] in pipeline_state:
#             css_class, status_label = "step-done", "✔ Done"
#         elif idx == active_step:
#             css_class, status_label = "step-active", "⏳ Running…"
#         else:
#             css_class, status_label = "step-pending", "Pending"

#         with col:
#             st.markdown(
#                 f'<div class="step-card {css_class}">'
#                 f'{step["icon"]}<br>{step["label"]}<br>'
#                 f'<span style="font-size:0.72rem;font-weight:400">{status_label}</span>'
#                 f'</div>',
#                 unsafe_allow_html=True,
#             )


# def render_result_box(
#     title: str,
#     content: str | None,
#     icon: str = "",
#     done: bool = False,
#     running: bool = False,
# ) -> None:
#     """Render a single labelled result box with monospace scrollable content."""
#     st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)

#     if content and content.strip():
#         extra_class = "result-box-done" if done else ""
#         st.markdown(
#             f'<div class="result-box {extra_class}">{content}</div>',
#             unsafe_allow_html=True,
#         )
#     elif running:
#         st.markdown(
#             '<div class="result-box result-running">⏳ Running… please wait</div>',
#             unsafe_allow_html=True,
#         )
#     else:
#         st.markdown(
#             '<div class="result-box result-empty">Waiting for this step to complete…</div>',
#             unsafe_allow_html=True,
#         )


# def render_all_result_boxes(pipeline_state: dict, active_step: int = -1) -> None:
#     """Render all four result boxes in a 2-column layout."""
#     col_left, col_right = st.columns(2, gap="medium")
#     left_keys  = ["search_results", "report"]
#     right_keys = ["scraped_content", "feedback"]

#     # Resolve which key is currently active
#     active_key = STEPS[active_step]["key"] if 0 <= active_step < len(STEPS) else None

#     with col_left:
#         for meta in RESULT_META:
#             if meta["key"] in left_keys:
#                 content = pipeline_state.get(meta["key"])
#                 render_result_box(
#                     meta["title"],
#                     content,
#                     meta["icon"],
#                     done=bool(content),
#                     running=(meta["key"] == active_key and not content),
#                 )

#     with col_right:
#         for meta in RESULT_META:
#             if meta["key"] in right_keys:
#                 content = pipeline_state.get(meta["key"])
#                 render_result_box(
#                     meta["title"],
#                     content,
#                     meta["icon"],
#                     done=bool(content),
#                     running=(meta["key"] == active_key and not content),
#                 )


# def render_download_button(topic: str, pipeline_state: dict) -> None:
#     """Show a download button for the final report if available."""
#     report_text = pipeline_state.get("report", "").strip()
#     if not report_text:
#         return
#     safe_topic = topic.strip().replace(" ", "_")[:60]
#     full_content = (
#         f"Research Topic: {topic}\n{'='*60}\n\n"
#         f"FINAL REPORT\n{'='*60}\n{report_text}\n\n"
#         f"CRITIC FEEDBACK\n{'='*60}\n{pipeline_state.get('feedback', 'N/A')}\n"
#     )
#     st.download_button(
#         label="⬇️ Download Report (.txt)",
#         data=full_content.encode("utf-8"),
#         file_name=f"report_{safe_topic}.txt",
#         mime="text/plain",
#     )


# # ---------------------------------------------------------------------------
# # Main
# # ---------------------------------------------------------------------------

# def main() -> None:
#     """Entry point – builds the full Streamlit page."""
#     st.set_page_config(page_title="Research Pipeline", page_icon="🔬", layout="wide")
#     st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
#     init_session_state()

#     # ── Header ───────────────────────────────────────────────────────────────
#     st.title("🔬 AI Research Pipeline")
#     st.caption("Enter a topic and watch each step complete live — search, scrape, write, critique.")
#     st.divider()

#     # ── Input row ────────────────────────────────────────────────────────────
#     input_col, button_col = st.columns([4, 1], gap="small")
#     with input_col:
#         topic_input = st.text_input(
#             label="Research Topic",
#             value=st.session_state.topic,
#             placeholder="e.g. Impact of climate change on coastal cities",
#             max_chars=MAX_TOPIC_LENGTH,
#             label_visibility="collapsed",
#         )
#     with button_col:
#         run_clicked = st.button("▶ Run", use_container_width=True)

#     # ── Validation & trigger ─────────────────────────────────────────────────
#     if run_clicked:
#         err = validate_topic(topic_input)
#         if err:
#             st.warning(err)
#         else:
#             st.session_state.topic = topic_input.strip()
#             st.session_state.pipeline_state = {}
#             st.session_state.active_step = -1
#             st.session_state.error = None
#             st.session_state.running = True

#     # ── Error display ─────────────────────────────────────────────────────────
#     if st.session_state.error:
#         st.error(
#             f"❌ Pipeline failed: {st.session_state.error}\n\n"
#             "Check your API keys, network connection, and try again."
#         )

#     # ── Progress tracker placeholder ──────────────────────────────────────────
#     st.subheader("Pipeline Progress")
#     tracker_placeholder = st.empty()
#     with tracker_placeholder.container():
#         render_step_tracker(
#             st.session_state.pipeline_state,
#             st.session_state.active_step,
#         )
#     st.divider()

#     # ── Result boxes placeholder ───────────────────────────────────────────────
#     results_placeholder = st.empty()

#     # ── Execute pipeline live (step-by-step with UI updates) ──────────────────
#     if st.session_state.running:
#         st.session_state.running = False
#         with results_placeholder.container():
#             render_all_result_boxes({})          # show empty boxes immediately
#         execute_pipeline_live(
#             st.session_state.topic,
#             tracker_placeholder,
#             results_placeholder,
#         )

#     # ── Render persisted results on reload (after pipeline already ran) ────────
#     elif st.session_state.pipeline_state:
#         with results_placeholder.container():
#             render_all_result_boxes(st.session_state.pipeline_state)

#     else:
#         st.info("Enter a topic above and click **▶ Run** to start the pipeline.")

#     # ── Download button ───────────────────────────────────────────────────────
#     if st.session_state.pipeline_state.get("report"):
#         st.divider()
#         render_download_button(st.session_state.topic, st.session_state.pipeline_state)


# if __name__ == "__main__":
#     main()



# # =============================================================================
# # Research Pipeline – Streamlit Frontend
# # =============================================================================

# import traceback
# import streamlit as st
# from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

# # ---------------------------------------------------------------------------
# # Constants
# # ---------------------------------------------------------------------------

# MAX_TOPIC_LENGTH = 300

# STEPS = [
#     {"key": "search_results",  "label": "Web Search",       "icon": "🔍"},
#     {"key": "scraped_content", "label": "Reader / Scraper",  "icon": "📄"},
#     {"key": "report",          "label": "Writer",            "icon": "✍️"},
#     {"key": "feedback",        "label": "Critic",            "icon": "🧐"},
# ]

# RESULT_META = [
#     {"key": "search_results",  "title": "Web Search Results", "icon": "🔍"},
#     {"key": "scraped_content", "title": "Scraped Content",    "icon": "📄"},
#     {"key": "report",          "title": "Final Report",       "icon": "✍️"},
#     {"key": "feedback",        "title": "Critic Feedback",    "icon": "🧐"},
# ]

# # ---------------------------------------------------------------------------
# # CSS
# # ---------------------------------------------------------------------------

# CUSTOM_CSS = """
# <style>
# [data-testid="stAppViewContainer"] { background: #f7f8fc; }
# [data-testid="stSidebar"] { display: none; }

# .step-card {
#     border-radius: 12px;
#     padding: 14px 10px;
#     text-align: center;
#     font-size: 0.82rem;
#     font-weight: 600;
#     border: 2px solid transparent;
#     transition: all 0.25s ease;
#     margin-bottom: 4px;
# }
# .step-pending { background: #e9ecef; color: #868e96; border-color: #dee2e6; }
# .step-active  { background: #fff3cd; color: #856404; border-color: #ffc107;
#                 box-shadow: 0 0 0 3px rgba(255,193,7,0.25); }
# .step-done    { background: #d1e7dd; color: #0a3622; border-color: #86c9a4; }

# .result-box {
#     background: #ffffff;
#     border: 1px solid #dee2e6;
#     border-radius: 10px;
#     padding: 16px 18px;
#     font-family: 'Courier New', Courier, monospace;
#     font-size: 0.82rem;
#     line-height: 1.6;
#     min-height: 340px;
#     max-height: 340px;
#     overflow-y: auto;
#     white-space: pre-wrap;
#     word-break: break-word;
#     color: #212529;
#     margin-bottom: 12px;
# }
# .result-box-done {
#     border-color: #86c9a4 !important;
#     border-width: 2px !important;
# }
# .result-running {
#     color: #856404 !important;
#     font-style: italic;
#     font-family: sans-serif !important;
#     background: #fff3cd !important;
#     border-color: #ffc107 !important;
#     border-width: 2px !important;
#     display: flex !important;
#     align-items: center !important;
#     justify-content: center !important;
#     font-size: 0.95rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.02em;
# }
# .result-empty {
#     color: #adb5bd;
#     font-style: italic;
#     font-family: sans-serif;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     height: 100%;
# }
# .section-title {
#     font-size: 1rem;
#     font-weight: 700;
#     color: #343a40;
#     margin-bottom: 6px;
# }

# /* ── Action buttons row ── */
# div[data-testid="stButton"] > button {
#     background: #4361ee; color: #fff; border: none;
#     border-radius: 8px; padding: 0.55rem 2rem;
#     font-size: 1rem; font-weight: 600; width: 100%;
#     transition: background 0.2s;
# }
# div[data-testid="stButton"] > button:hover { background: #3251d3; }

# div[data-testid="stDownloadButton"] > button {
#     background: #2dc653; color: #fff; border: none;
#     border-radius: 8px; padding: 0.5rem 1.6rem;
#     font-weight: 600; transition: background 0.2s;
# }
# div[data-testid="stDownloadButton"] > button:hover { background: #24a845; }

# /* ── Modal dialog content ── */
# .modal-report {
#     background: #ffffff;
#     border-radius: 12px;
#     padding: 8px 4px;
#     font-family: 'Georgia', serif;
#     font-size: 0.97rem;
#     line-height: 1.85;
#     color: #212529;
# }
# .modal-feedback {
#     background: #ffffff;
#     border-radius: 12px;
#     padding: 8px 4px;
#     font-family: 'Segoe UI', sans-serif;
#     font-size: 0.95rem;
#     line-height: 1.8;
#     color: #212529;
# }
# .modal-section-header {
#     font-size: 1.1rem;
#     font-weight: 700;
#     color: #4361ee;
#     margin-top: 1.2rem;
#     margin-bottom: 0.3rem;
#     border-bottom: 2px solid #e9ecef;
#     padding-bottom: 4px;
# }
# .modal-topic-badge {
#     display: inline-block;
#     background: #e7f5ff;
#     color: #1971c2;
#     border-radius: 20px;
#     padding: 4px 14px;
#     font-size: 0.82rem;
#     font-weight: 600;
#     margin-bottom: 16px;
# }
# .feedback-block {
#     background: #f8f9fa;
#     border-left: 4px solid #4361ee;
#     border-radius: 0 8px 8px 0;
#     padding: 12px 16px;
#     margin-bottom: 12px;
#     font-size: 0.93rem;
#     line-height: 1.75;
#     color: #343a40;
# }
# </style>
# """

# # ---------------------------------------------------------------------------
# # Session-state helpers
# # ---------------------------------------------------------------------------

# def init_session_state() -> None:
#     defaults: dict = {
#         "topic": "",
#         "pipeline_state": {},
#         "active_step": -1,
#         "running": False,
#         "error": None,
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value


# # ---------------------------------------------------------------------------
# # Validation
# # ---------------------------------------------------------------------------

# def validate_topic(topic: str) -> str | None:
#     stripped = topic.strip()
#     if not stripped:
#         return "Please enter a research topic before running."
#     if len(stripped) > MAX_TOPIC_LENGTH:
#         return f"Topic is too long (max {MAX_TOPIC_LENGTH} characters)."
#     return None


# # ---------------------------------------------------------------------------
# # Individual step runners
# # ---------------------------------------------------------------------------

# def run_step_search(topic: str) -> str:
#     agent = build_search_agent()
#     result = agent.invoke({
#         "messages": [(
#             "user",
#             f"Find recent and reliable information on the topic: {topic} "
#             "using the web search tool and return the info in structured format."
#         )]
#     })
#     return result["messages"][-1].content


# def run_step_reader(topic: str, search_results: str) -> str:
#     agent = build_reader_agent()
#     result = agent.invoke({
#         "messages": [(
#             "user",
#             f"Based on the following search results about '{topic}', "
#             "pick the most relevant URL and scrape it for deeper content.\n\n"
#             f"Search Results:\n{search_results[:800]}"
#         )]
#     })
#     return result["messages"][-1].content


# def run_step_writer(topic: str, search_results: str, scraped_content: str) -> str:
#     combined = (
#         f"SEARCH RESULTS:\n{search_results}\n\n"
#         f"DETAILED SCRAPED CONTENT:\n{scraped_content}\n\n"
#     )
#     return writer_chain.invoke({"topic": topic, "research": combined})


# def run_step_critic(report: str) -> str:
#     return critic_chain.invoke({"report": report})


# # ---------------------------------------------------------------------------
# # Live pipeline executor
# # ---------------------------------------------------------------------------

# def execute_pipeline_live(
#     topic: str,
#     tracker_placeholder: st.delta_generator.DeltaGenerator,
#     results_placeholder: st.delta_generator.DeltaGenerator,
# ) -> None:
#     state: dict = {}
#     st.session_state.pipeline_state = {}
#     st.session_state.error = None

#     def step_fn_search():
#         return run_step_search(topic)

#     def step_fn_reader():
#         return run_step_reader(topic, state["search_results"])

#     def step_fn_writer():
#         return run_step_writer(topic, state["search_results"], state["scraped_content"])

#     def step_fn_critic():
#         return run_step_critic(state["report"])

#     step_functions = [step_fn_search, step_fn_reader, step_fn_writer, step_fn_critic]

#     for step_index, (step_meta, step_fn) in enumerate(zip(STEPS, step_functions)):
#         st.session_state.active_step = step_index

#         with tracker_placeholder.container():
#             render_step_tracker(state, step_index)

#         with results_placeholder.container():
#             render_all_result_boxes(state, active_step=step_index)

#         try:
#             output = step_fn()
#         except Exception as exc:
#             st.session_state.error = str(exc)
#             st.session_state.active_step = -1
#             traceback.print_exc()
#             return

#         state[step_meta["key"]] = output
#         st.session_state.pipeline_state = dict(state)

#         with tracker_placeholder.container():
#             render_step_tracker(state, step_index + 1)

#         with results_placeholder.container():
#             render_all_result_boxes(state)

#     st.session_state.active_step = len(STEPS)


# # ---------------------------------------------------------------------------
# # UI rendering helpers
# # ---------------------------------------------------------------------------

# def render_step_tracker(pipeline_state: dict, active_step: int) -> None:
#     cols = st.columns(len(STEPS))
#     for idx, (step, col) in enumerate(zip(STEPS, cols)):
#         if step["key"] in pipeline_state:
#             css_class, status_label = "step-done", "✔ Done"
#         elif idx == active_step:
#             css_class, status_label = "step-active", "⏳ Running…"
#         else:
#             css_class, status_label = "step-pending", "Pending"

#         with col:
#             st.markdown(
#                 f'<div class="step-card {css_class}">'
#                 f'{step["icon"]}<br>{step["label"]}<br>'
#                 f'<span style="font-size:0.72rem;font-weight:400">{status_label}</span>'
#                 f'</div>',
#                 unsafe_allow_html=True,
#             )


# def render_result_box(
#     title: str,
#     content: str | None,
#     icon: str = "",
#     done: bool = False,
#     running: bool = False,
# ) -> None:
#     st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)

#     if content and content.strip():
#         extra_class = "result-box-done" if done else ""
#         st.markdown(
#             f'<div class="result-box {extra_class}">{content}</div>',
#             unsafe_allow_html=True,
#         )
#     elif running:
#         st.markdown(
#             '<div class="result-box result-running">⏳ Running… please wait</div>',
#             unsafe_allow_html=True,
#         )
#     else:
#         st.markdown(
#             '<div class="result-box result-empty">Waiting for this step to complete…</div>',
#             unsafe_allow_html=True,
#         )


# def render_all_result_boxes(pipeline_state: dict, active_step: int = -1) -> None:
#     col_left, col_right = st.columns(2, gap="medium")
#     left_keys  = ["search_results", "report"]
#     right_keys = ["scraped_content", "feedback"]

#     active_key = STEPS[active_step]["key"] if 0 <= active_step < len(STEPS) else None

#     with col_left:
#         for meta in RESULT_META:
#             if meta["key"] in left_keys:
#                 content = pipeline_state.get(meta["key"])
#                 render_result_box(
#                     meta["title"], content, meta["icon"],
#                     done=bool(content),
#                     running=(meta["key"] == active_key and not content),
#                 )

#     with col_right:
#         for meta in RESULT_META:
#             if meta["key"] in right_keys:
#                 content = pipeline_state.get(meta["key"])
#                 render_result_box(
#                     meta["title"], content, meta["icon"],
#                     done=bool(content),
#                     running=(meta["key"] == active_key and not content),
#                 )


# # ---------------------------------------------------------------------------
# # Modal dialogs
# # ---------------------------------------------------------------------------

# @st.dialog("📄 Final Report", width="large")
# def show_report_modal(topic: str, report: str) -> None:
#     """Render the final report in a clean readable dialog."""
#     st.markdown(
#         f'<div class="modal-topic-badge">🔬 {topic}</div>',
#         unsafe_allow_html=True,
#     )
#     # Render markdown so headers, bold, bullets all display properly
#     st.markdown('<div class="modal-report">', unsafe_allow_html=True)
#     st.markdown(report)
#     st.markdown('</div>', unsafe_allow_html=True)

#     st.divider()
#     safe_topic = topic.strip().replace(" ", "_")[:60]
#     st.download_button(
#         label="⬇️ Download Report (.txt)",
#         data=report.encode("utf-8"),
#         file_name=f"report_{safe_topic}.txt",
#         mime="text/plain",
#         use_container_width=True,
#     )


# @st.dialog("🧐 Critic Feedback", width="large")
# def show_feedback_modal(topic: str, feedback: str) -> None:
#     """Render critic feedback in a clean readable dialog."""
#     st.markdown(
#         f'<div class="modal-topic-badge">🔬 {topic}</div>',
#         unsafe_allow_html=True,
#     )

#     # Split feedback into paragraphs and render each as a styled block
#     st.markdown('<div class="modal-feedback">', unsafe_allow_html=True)
#     paragraphs = [p.strip() for p in feedback.split("\n") if p.strip()]
#     for para in paragraphs:
#         # Treat lines starting with # as section headers
#         if para.startswith("#"):
#             clean = para.lstrip("#").strip()
#             st.markdown(
#                 f'<div class="modal-section-header">{clean}</div>',
#                 unsafe_allow_html=True,
#             )
#         else:
#             st.markdown(
#                 f'<div class="feedback-block">{para}</div>',
#                 unsafe_allow_html=True,
#             )
#     st.markdown('</div>', unsafe_allow_html=True)


# # ---------------------------------------------------------------------------
# # Download button
# # ---------------------------------------------------------------------------

# def render_download_button(topic: str, pipeline_state: dict) -> None:
#     report_text = pipeline_state.get("report", "").strip()
#     if not report_text:
#         return
#     safe_topic = topic.strip().replace(" ", "_")[:60]
#     full_content = (
#         f"Research Topic: {topic}\n{'='*60}\n\n"
#         f"FINAL REPORT\n{'='*60}\n{report_text}\n\n"
#         f"CRITIC FEEDBACK\n{'='*60}\n{pipeline_state.get('feedback', 'N/A')}\n"
#     )
#     st.download_button(
#         label="⬇️ Download Full Report (.txt)",
#         data=full_content.encode("utf-8"),
#         file_name=f"report_{safe_topic}.txt",
#         mime="text/plain",
#     )


# # ---------------------------------------------------------------------------
# # Main
# # ---------------------------------------------------------------------------

# def main() -> None:
#     st.set_page_config(page_title="Research Pipeline", page_icon="🔬", layout="wide")
#     st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
#     init_session_state()

#     # ── Header ───────────────────────────────────────────────────────────────
#     st.title("🔬 AI Research Pipeline")
#     st.caption("Enter a topic and watch each step complete live — search, scrape, write, critique.")
#     st.divider()

#     # ── Input row ────────────────────────────────────────────────────────────
#     input_col, button_col = st.columns([4, 1], gap="small")
#     with input_col:
#         topic_input = st.text_input(
#             label="Research Topic",
#             value=st.session_state.topic,
#             placeholder="e.g. Impact of climate change on coastal cities",
#             max_chars=MAX_TOPIC_LENGTH,
#             label_visibility="collapsed",
#         )
#     with button_col:
#         run_clicked = st.button("▶ Run", use_container_width=True)

#     # ── Validation & trigger ─────────────────────────────────────────────────
#     if run_clicked:
#         err = validate_topic(topic_input)
#         if err:
#             st.warning(err)
#         else:
#             st.session_state.topic = topic_input.strip()
#             st.session_state.pipeline_state = {}
#             st.session_state.active_step = -1
#             st.session_state.error = None
#             st.session_state.running = True

#     # ── Error display ─────────────────────────────────────────────────────────
#     if st.session_state.error:
#         st.error(
#             f"❌ Pipeline failed: {st.session_state.error}\n\n"
#             "Check your API keys, network connection, and try again."
#         )

#     # ── Progress tracker placeholder ──────────────────────────────────────────
#     st.subheader("Pipeline Progress")
#     tracker_placeholder = st.empty()
#     with tracker_placeholder.container():
#         render_step_tracker(
#             st.session_state.pipeline_state,
#             st.session_state.active_step,
#         )
#     st.divider()

#     # ── Result boxes placeholder ───────────────────────────────────────────────
#     results_placeholder = st.empty()

#     # ── Execute pipeline live ─────────────────────────────────────────────────
#     if st.session_state.running:
#         st.session_state.running = False
#         with results_placeholder.container():
#             render_all_result_boxes({})
#         execute_pipeline_live(
#             st.session_state.topic,
#             tracker_placeholder,
#             results_placeholder,
#         )

#     elif st.session_state.pipeline_state:
#         with results_placeholder.container():
#             render_all_result_boxes(st.session_state.pipeline_state)

#     else:
#         st.info("Enter a topic above and click **▶ Run** to start the pipeline.")

#     # ── Bottom action bar (only when pipeline is complete) ────────────────────
#     pipeline_state = st.session_state.pipeline_state
#     report_ready   = bool(pipeline_state.get("report", "").strip())
#     feedback_ready = bool(pipeline_state.get("feedback", "").strip())

#     if report_ready or feedback_ready:
#         st.divider()
#         action_cols = st.columns([1, 1, 2], gap="small")

#         with action_cols[0]:
#             if report_ready:
#                 if st.button("📄 Final Report", use_container_width=True):
#                     show_report_modal(st.session_state.topic, pipeline_state["report"])

#         with action_cols[1]:
#             if feedback_ready:
#                 if st.button("🧐 Critic Feedback", use_container_width=True):
#                     show_feedback_modal(st.session_state.topic, pipeline_state["feedback"])

#         with action_cols[2]:
#             if report_ready:
#                 render_download_button(st.session_state.topic, pipeline_state)


# if __name__ == "__main__":
#     main()






print("new code")



# =============================================================================
# Research Pipeline – Streamlit Frontend
# =============================================================================

import traceback
import streamlit as st
import os

# --- SECRET SYNC FOR STREAMLIT CLOUD ---
# Ensure secrets entered in the Streamlit Cloud dashboard are pushed into the OS environment 
# so that Langchain (OpenAI) and TavilyClient can detect them upon module import.
try:
    for k, v in st.secrets.items():
        if type(v) is str or type(v) is int or type(v) is float:
            os.environ[str(k)] = str(v)
except Exception:
    pass
# ---------------------------------------

from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MAX_TOPIC_LENGTH = 300

STEPS = [
    {"key": "search_results",  "label": "Web Search",       "icon": "🔍"},
    {"key": "scraped_content", "label": "Reader / Scraper",  "icon": "📄"},
    {"key": "report",          "label": "Writer",            "icon": "✍️"},
    {"key": "feedback",        "label": "Critic",            "icon": "🧐"},
]

RESULT_META = [
    {"key": "search_results",  "title": "Web Search Results", "icon": "🔍"},
    {"key": "scraped_content", "title": "Scraped Content",    "icon": "📄"},
    {"key": "report",          "title": "Final Report",       "icon": "✍️"},
    {"key": "feedback",        "title": "Critic Feedback",    "icon": "🧐"},
]

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&family=Space+Mono:wght@400;700&display=swap');

/* Main App Background & Font */
[data-testid="stAppViewContainer"] { 
    background: #f8fafc; 
    font-family: 'Outfit', sans-serif;
    color: #0f172a;
}
[data-testid="stSidebar"] { display: none; }

/* Custom Heading styles */
.hero-container {
    text-align: center;
    padding: 3rem 1rem 2rem 1rem;
}
.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.2;
    background: linear-gradient(135deg, #9f1239, #e11d48, #f43f5e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}
.hero-subtitle {
    font-size: 1.1rem;
    color: #64748b;
    margin-bottom: 2rem;
    font-weight: 300;
}

/* Beautiful Search Input */
div[data-testid="stTextInput"] input {
    background: #ffffff !important;
    border: 2px solid #cbd5e1 !important;
    border-radius: 12px !important;
    padding: 0.8rem 1.2rem !important;
    font-size: 1.1rem !important;
    color: #0f172a !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
}
div[data-testid="stTextInput"] input:focus {
    border-color: #be123c !important;
    box-shadow: 0 0 0 4px rgba(190, 18, 60, 0.2) !important;
    outline: none !important;
    transform: translateY(-2px);
}
div[data-testid="stTextInput"] input::placeholder {
    color: #94a3b8 !important;
}

/* Primary Run Button */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #e11d48 0%, #9f1239 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.8rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 14px 0 rgba(190, 18, 60, 0.3) !important;
    transition: all 0.3s ease !important;
    height: 100%;
}
div[data-testid="stButton"] > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(190, 18, 60, 0.4) !important;
}
div[data-testid="stButton"] > button[kind="primary"]:active {
    transform: translateY(1px);
}

/* Step cards styling */
.step-card {
    border-radius: 16px;
    padding: 16px 12px;
    text-align: center;
    font-size: 0.85rem;
    font-weight: 500;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    margin-bottom: 8px;
    background: #ffffff;
    color: #64748b;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.step-pending { border-color: #cbd5e1; }
.step-active  { 
    background: rgba(190, 18, 60, 0.05); 
    color: #be123c; 
    border-color: #e11d48;
    box-shadow: 0 0 15px rgba(225, 29, 72, 0.15);
}
.step-done    { 
    background: rgba(34,197,94,0.05); 
    color: #16a34a; 
    border-color: #22c55e; 
}

/* Result Box */
.result-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 12px;
    padding: 18px 22px;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    line-height: 1.6;
    min-height: 340px;
    max-height: 340px;
    overflow-y: auto;
    white-space: pre-wrap;
    word-break: break-word;
    color: #334155;
    margin-bottom: 16px;
    box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);
}
.result-box-done {
    border-color: #22c55e !important;
}
.result-running {
    color: #e11d48 !important;
    font-family: 'Outfit', sans-serif !important;
    background: rgba(225, 29, 72, 0.05) !important;
    border-color: #e11d48 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.05rem !important;
    font-weight: 500 !important;
}
.result-empty {
    color: #94a3b8;
    font-family: 'Outfit', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}
.section-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 8px;
    letter-spacing: 0.02em;
}

/* Download button (active everywhere) */
div[data-testid="stDownloadButton"] > button {
    background: #10b981; color: #fff; border: none;
    border-radius: 12px; padding: 0.6rem 1.6rem;
    font-weight: 700; transition: all 0.3s ease;
    width: 100%; box-shadow: 0 4px 10px rgba(16, 185, 129, 0.25);
}
div[data-testid="stDownloadButton"] > button:hover {
    background: #059669; transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(16, 185, 129, 0.35);
}

/* Modal content */
.modal-report {
    background: #ffffff;
    border-radius: 12px;
    padding: 16px;
    font-family: 'Space Mono', monospace;
    font-size: 0.95rem;
    line-height: 1.7;
    color: #334155;
}
.modal-feedback {
    background: #ffffff;
    border-radius: 12px;
    padding: 16px;
    font-family: 'Outfit', sans-serif;
    font-size: 1.05rem;
    line-height: 1.7;
    color: #334155;
}
.modal-section-header {
    font-size: 1.2rem;
    font-weight: 700;
    color: #be123c;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 6px;
}
.modal-topic-badge {
    display: inline-block;
    background: rgba(190, 18, 60, 0.08);
    color: #9f1239;
    border: 1px solid rgba(190, 18, 60, 0.15);
    border-radius: 20px;
    padding: 6px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 16px;
}
.feedback-block {
    background: #f8fafc;
    border-left: 4px solid #e11d48;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin-bottom: 14px;
    font-size: 1rem;
    line-height: 1.7;
    color: #1e293b;
}
</style>
"""

# ---------------------------------------------------------------------------
# Session-state helpers
# ---------------------------------------------------------------------------

def init_session_state() -> None:
    defaults: dict = {
        "topic": "",
        "pipeline_state": {},
        "active_step": -1,
        "running": False,
        "error": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_topic(topic: str) -> str | None:
    stripped = topic.strip()
    if not stripped:
        return "Please enter a research topic before running."
    if len(stripped) > MAX_TOPIC_LENGTH:
        return f"Topic is too long (max {MAX_TOPIC_LENGTH} characters)."
    return None


# ---------------------------------------------------------------------------
# Individual step runners
# ---------------------------------------------------------------------------

def run_step_search(topic: str) -> str:
    print("\n" + "="*50)
    print("STEP 1 - search agent working ...")
    print("="*50)
    agent = build_search_agent()
    result = agent.invoke({
        "messages": [(
            "user",
            f"Find recent and reliable information on the topic: {topic} "
            "using the web search tool and return the info in structured format."
        )]
    })
    content = result["messages"][-1].content
    print(f"\n search result: {content}\n")
    return content


def run_step_reader(topic: str, search_results: str) -> str:
    print("\n" + "="*50)
    print("STEP 2 - reader agent is scraping top resources ...")
    print("="*50)
    agent = build_reader_agent()
    result = agent.invoke({
        "messages": [(
            "user",
            f"Based on the following search results about '{topic}', "
            "pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{search_results[:800]}"
        )]
    })
    content = result["messages"][-1].content
    print(f"\n scraped content: {content}\n")
    return content


def run_step_writer(topic: str, search_results: str, scraped_content: str) -> str:
    print("\n" + "="*50)
    print("STEP 3 - writer is drafting the report ...")
    print("="*50)
    combined = (
        f"SEARCH RESULTS:\n{search_results}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{scraped_content}\n\n"
    )
    report = writer_chain.invoke({"topic": topic, "research": combined})
    print(f"\n Final report: {report}\n")
    return report


def run_step_critic(report: str) -> str:
    print("\n" + "="*50)
    print("STEP 4 - critic is evaluating the report ...")
    print("="*50)
    feedback = critic_chain.invoke({"report": report})
    print(f"\n Critic's review: {feedback}\n")
    return feedback


# ---------------------------------------------------------------------------
# Live pipeline executor
# ---------------------------------------------------------------------------

def execute_pipeline_live(
    topic: str,
    tracker_placeholder: st.delta_generator.DeltaGenerator,
    results_placeholder: st.delta_generator.DeltaGenerator,
) -> None:
    state: dict = {}
    st.session_state.pipeline_state = {}
    st.session_state.error = None

    def step_fn_search():
        return run_step_search(topic)

    def step_fn_reader():
        return run_step_reader(topic, state["search_results"])

    def step_fn_writer():
        return run_step_writer(topic, state["search_results"], state["scraped_content"])

    def step_fn_critic():
        return run_step_critic(state["report"])

    step_functions = [step_fn_search, step_fn_reader, step_fn_writer, step_fn_critic]

    for step_index, (step_meta, step_fn) in enumerate(zip(STEPS, step_functions)):
        st.session_state.active_step = step_index

        with tracker_placeholder.container():
            render_step_tracker(state, step_index)

        with results_placeholder.container():
            render_all_result_boxes(state, active_step=step_index)

        try:
            output = step_fn()
        except Exception as exc:
            st.session_state.error = str(exc)
            st.session_state.active_step = -1
            traceback.print_exc()
            return

        state[step_meta["key"]] = output
        st.session_state.pipeline_state = dict(state)

        with tracker_placeholder.container():
            render_step_tracker(state, step_index + 1)

        with results_placeholder.container():
            render_all_result_boxes(state)

    st.session_state.active_step = len(STEPS)


# ---------------------------------------------------------------------------
# UI rendering helpers
# ---------------------------------------------------------------------------

def render_step_tracker(pipeline_state: dict, active_step: int) -> None:
    cols = st.columns(len(STEPS))
    for idx, (step, col) in enumerate(zip(STEPS, cols)):
        if step["key"] in pipeline_state:
            css_class, status_label = "step-done", "✔ Done"
        elif idx == active_step:
            css_class, status_label = "step-active", "⏳ Running…"
        else:
            css_class, status_label = "step-pending", "Pending"

        with col:
            st.markdown(
                f'<div class="step-card {css_class}">'
                f'{step["icon"]}<br>{step["label"]}<br>'
                f'<span style="font-size:0.72rem;font-weight:400">{status_label}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )


def render_result_box(
    title: str,
    content: str | None,
    icon: str = "",
    done: bool = False,
    running: bool = False,
) -> None:
    st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)

    if content and content.strip():
        extra_class = "result-box-done" if done else ""
        st.markdown(
            f'<div class="result-box {extra_class}">{content}</div>',
            unsafe_allow_html=True,
        )
    elif running:
        st.markdown(
            '<div class="result-box result-running">⏳ Running… please wait</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="result-box result-empty">Waiting for previous steps to complete…</div>',
            unsafe_allow_html=True,
        )


def render_all_result_boxes(pipeline_state: dict, active_step: int = -1) -> None:
    col_left, col_right = st.columns(2, gap="medium")
    left_keys  = ["search_results", "report"]
    right_keys = ["scraped_content", "feedback"]

    active_key = STEPS[active_step]["key"] if 0 <= active_step < len(STEPS) else None

    with col_left:
        for meta in RESULT_META:
            if meta["key"] in left_keys:
                content = pipeline_state.get(meta["key"])
                render_result_box(
                    meta["title"], content, meta["icon"],
                    done=bool(content),
                    running=(meta["key"] == active_key and not content),
                )

    with col_right:
        for meta in RESULT_META:
            if meta["key"] in right_keys:
                content = pipeline_state.get(meta["key"])
                render_result_box(
                    meta["title"], content, meta["icon"],
                    done=bool(content),
                    running=(meta["key"] == active_key and not content),
                )


# ---------------------------------------------------------------------------
# Modal dialogs
# ---------------------------------------------------------------------------

@st.dialog("📄 Final Report", width="large")
def show_report_modal(topic: str, report: str) -> None:
    st.markdown(
        f'<div class="modal-topic-badge">🔬 {topic}</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="modal-report">', unsafe_allow_html=True)
    st.markdown(report)
    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()
    safe_topic = topic.strip().replace(" ", "_")[:60]
    st.download_button(
        label="⬇️ Download Report (.txt)",
        data=report.encode("utf-8"),
        file_name=f"report_{safe_topic}.txt",
        mime="text/plain",
        use_container_width=True,
    )


@st.dialog("🧐 Critic Feedback", width="large")
def show_feedback_modal(topic: str, feedback: str) -> None:
    st.markdown(
        f'<div class="modal-topic-badge">🔬 {topic}</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="modal-feedback">', unsafe_allow_html=True)
    paragraphs = [p.strip() for p in feedback.split("\n") if p.strip()]
    for para in paragraphs:
        if para.startswith("#"):
            clean = para.lstrip("#").strip()
            st.markdown(
                f'<div class="modal-section-header">{clean}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="feedback-block">{para}</div>',
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Download button
# ---------------------------------------------------------------------------

def render_download_button(topic: str, pipeline_state: dict) -> None:
    report_text = pipeline_state.get("report", "").strip()
    if not report_text:
        return
    safe_topic = topic.strip().replace(" ", "_")[:60]
    full_content = (
        f"Research Topic: {topic}\n{'='*60}\n\n"
        f"FINAL REPORT\n{'='*60}\n{report_text}\n\n"
        f"CRITIC FEEDBACK\n{'='*60}\n{pipeline_state.get('feedback', 'N/A')}\n"
    )
    st.download_button(
        label="⬇️ Download Full Report",
        data=full_content.encode("utf-8"),
        file_name=f"report_{safe_topic}.txt",
        mime="text/plain",
        use_container_width=True,
    )


# ---------------------------------------------------------------------------
# Top action bar
# ---------------------------------------------------------------------------

def render_top_action_bar(topic: str, pipeline_state: dict) -> None:
    """
    Renders the three action buttons (Final Report, Critic Feedback, Download)
    just below the input row. Buttons are grey/disabled before pipeline runs,
    green and clickable once the relevant output is ready.
    """
    report_ready   = bool(pipeline_state.get("report", "").strip())
    feedback_ready = bool(pipeline_state.get("feedback", "").strip())

    # ── Dynamic Styles for Action Buttons ──
    report_bg = "#2563eb" if report_ready else "#eff6ff"
    report_color = "#ffffff" if report_ready else "#60a5fa"
    report_border = "none" if report_ready else "1px solid #bfdbfe"
    report_hover = "#1d4ed8" if report_ready else "#eff6ff"

    feedback_bg = "#0d9488" if feedback_ready else "#f0fdfa"
    feedback_color = "#ffffff" if feedback_ready else "#2dd4bf"
    feedback_border = "none" if feedback_ready else "1px solid #99f6e4"
    feedback_hover = "#0f766e" if feedback_ready else "#f0fdfa"

    dl_bg = "#10b981" if report_ready else "#ecfdf5"
    dl_color = "#ffffff" if report_ready else "#34d399"
    dl_border = "none" if report_ready else "1px solid #a7f3d0"
    dl_hover = "#059669" if report_ready else "#ecfdf5"

    st.markdown(f'''
    <style>
    div[data-testid="column"]:nth-child(1) button[kind="secondary"] {{
        background: {report_bg} !important; color: {report_color} !important; border: {report_border} !important; border-radius: 12px; font-weight: 700; width: 100%; transition: all 0.3s;
    }}
    div[data-testid="column"]:nth-child(1) button[kind="secondary"] p,
    div[data-testid="column"]:nth-child(1) button[kind="secondary"] span {{ color: {report_color} !important; }}
    div[data-testid="column"]:nth-child(1) button[kind="secondary"]:hover {{ background: {report_hover} !important; transform: translateY(-2px); }}

    div[data-testid="column"]:nth-child(2) button[kind="secondary"] {{
        background: {feedback_bg} !important; color: {feedback_color} !important; border: {feedback_border} !important; border-radius: 12px; font-weight: 700; width: 100%; transition: all 0.3s;
    }}
    div[data-testid="column"]:nth-child(2) button[kind="secondary"] p,
    div[data-testid="column"]:nth-child(2) button[kind="secondary"] span {{ color: {feedback_color} !important; }}
    div[data-testid="column"]:nth-child(2) button[kind="secondary"]:hover {{ background: {feedback_hover} !important; transform: translateY(-2px); }}

    div[data-testid="column"]:nth-child(3) button[kind="secondary"] {{
        background: {dl_bg} !important; color: {dl_color} !important; border: {dl_border} !important; border-radius: 12px; font-weight: 700; width: 100%; transition: all 0.3s;
    }}
    div[data-testid="column"]:nth-child(3) button[kind="secondary"] p,
    div[data-testid="column"]:nth-child(3) button[kind="secondary"] span {{ color: {dl_color} !important; }}
    div[data-testid="column"]:nth-child(3) button[kind="secondary"]:hover {{ background: {dl_hover} !important; transform: translateY(-2px); }}
    </style>
    ''', unsafe_allow_html=True)

    col_report, col_feedback, col_download = st.columns(3, gap="small")

    # ── Final Report button ──────────────────────────────────────────────────
    report_label = "📄 Final Report" if report_ready else "⏳ Final Report (Pending)"
    with col_report:
        report_clicked = st.button(
            report_label,
            use_container_width=True,
            disabled=not report_ready,
            key="btn_report",
        )

    # ── Critic Feedback button ───────────────────────────────────────────────
    feedback_label = "🧐 Critic Feedback" if feedback_ready else "⏳ Critic Feedback (Pending)"
    with col_feedback:
        feedback_clicked = st.button(
            feedback_label,
            use_container_width=True,
            disabled=not feedback_ready,
            key="btn_feedback",
        )

    # ── Download button ──────────────────────────────────────────────────────
    download_label = "⬇️ Download Full Report" if report_ready else "⏳ Download Report (Pending)"
    with col_download:
        if report_ready:
            render_download_button(topic, pipeline_state)
        else:
            st.button(
                download_label,
                use_container_width=True,
                disabled=True,
                key="btn_download_disabled",
            )

    # ── Trigger modals after render ──────────────────────────────────────────
    if report_clicked and report_ready:
        show_report_modal(topic, pipeline_state["report"])

    if feedback_clicked and feedback_ready:
        show_feedback_modal(topic, pipeline_state["feedback"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    st.set_page_config(page_title="Research Pipeline", page_icon="🔬", layout="wide")
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    init_session_state()

    # ── Header ───────────────────────────────────────────────────────────────
    st.markdown('''
        <div class="hero-container">
            <div class="hero-title">🔬 AI Research Pipeline</div>
            <div class="hero-subtitle">Enter a topic and watch each step complete live — search, scrape, write, and critique.</div>
        </div>
    ''', unsafe_allow_html=True)

    # ── Input row ────────────────────────────────────────────────────────────
    input_col, button_col = st.columns([4, 1], gap="small")
    with input_col:
        topic_input = st.text_input(
            label="Research Topic",
            value=st.session_state.topic,
            placeholder="e.g. Impact of climate change on coastal cities",
            max_chars=MAX_TOPIC_LENGTH,
            label_visibility="collapsed",
        )
    with button_col:
        run_clicked = st.button("▶ Run", type="primary", use_container_width=True, key="btn_run")

    # ── Top action bar (always visible, grey until pipeline done) ─────────────
    st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)
    render_top_action_bar(st.session_state.topic, st.session_state.pipeline_state)

    st.divider()

    # ── Validation & trigger ─────────────────────────────────────────────────
    if run_clicked:
        err = validate_topic(topic_input)
        if err:
            st.warning(err)
        else:
            st.session_state.topic = topic_input.strip()
            st.session_state.pipeline_state = {}
            st.session_state.active_step = -1
            st.session_state.error = None
            st.session_state.running = True

    # ── Error display ─────────────────────────────────────────────────────────
    if st.session_state.error:
        st.error(
            f"❌ Pipeline failed: {st.session_state.error}\n\n"
            "Check your API keys, network connection, and try again."
        )

    # ── Progress tracker ──────────────────────────────────────────────────────
    st.subheader("Pipeline Progress")
    tracker_placeholder = st.empty()
    with tracker_placeholder.container():
        render_step_tracker(
            st.session_state.pipeline_state,
            st.session_state.active_step,
        )
    st.divider()

    # ── Result boxes placeholder ───────────────────────────────────────────────
    results_placeholder = st.empty()

    # ── Execute pipeline live ─────────────────────────────────────────────────
    if st.session_state.running:
        st.session_state.running = False
        with results_placeholder.container():
            render_all_result_boxes({})
        execute_pipeline_live(
            st.session_state.topic,
            tracker_placeholder,
            results_placeholder,
        )
        st.rerun()  # rerun so top bar re-renders green immediately

    elif st.session_state.pipeline_state:
        with results_placeholder.container():
            render_all_result_boxes(st.session_state.pipeline_state)

    else:
        st.info("Enter a topic above and click **▶ Run** to start the pipeline.")


if __name__ == "__main__":
    main()
