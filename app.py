"""Streamlit shell for a single-file deck built with build_deck.py.

Folder to deploy (GitHub → Streamlit Community Cloud):
    app.py                  this file: the presentation, at the app's address
    pages/1_Apresentador.py the presenter page, at <address>/Apresentador (script, who speaks, next, timer, ◀ ▶)
    deck.html               the built deck (dist/<name>.html, renamed)
    roteiro-*.pdf           the scripts from finish.py (optional: the presenter page offers them as downloads)
    requirements.txt        streamlit
    .streamlit/config.toml  dark base, minimal toolbar, no page menu

Local run:  streamlit run app.py

The deck fills the whole browser window; Streamlit's own chrome is hidden. Open the presenter page in another window
of the SAME browser (laptop screen) and this page fullscreen on the projector: the presenter page follows the deck and
moves it.
Keys work without clicking first: the deck engine listens on the host page too
(the iframe is same-origin). Change TITLE, and BACKDROP if the deck's letterbox
colour is not black.
"""
from pathlib import Path

import streamlit as st

TITLE = "Branquitude em foco"
BACKDROP = "#0F1117"
DECK = Path(__file__).parent / "deck.html"

st.set_page_config(page_title=TITLE, page_icon="▶", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    f"""
    <style>
      header, footer, #MainMenu,
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], [data-testid="stSidebar"], [data-testid="collapsedControl"],
      [data-testid="stSidebarCollapsedControl"], [data-testid="stAppDeployButton"], .stDeployButton {{ display: none !important; }}
      html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
        background: {BACKDROP} !important; overflow: hidden !important;
      }}
      .block-container, [data-testid="stMainBlockContainer"] {{ padding: 0 !important; max-width: 100% !important; }}
      iframe {{
        position: fixed !important; inset: 0 !important; z-index: 999990;
        width: 100vw !important; height: 100vh !important; height: 100dvh !important; border: 0 !important;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

if not DECK.exists():
    st.error("deck.html não encontrado ao lado de app.py. Gere com build_deck.py e copie para cá.")
    st.stop()

if hasattr(st, "iframe"):          # current API: embeds a local HTML file directly
    st.iframe(DECK, height=800)
else:                              # older Streamlit
    import streamlit.components.v1 as components

    components.html(DECK.read_text(encoding="utf-8"), height=800, scrolling=False)
