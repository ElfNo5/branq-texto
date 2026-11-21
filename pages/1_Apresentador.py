"""Presenter page of the Streamlit shell: the deck's script, following the presentation.

The app's address (app.py) is the presentation itself, fullscreen on the projector. <address>/Apresentador is this page,
for the laptop screen, in the SAME browser: who speaks now, the lines of this slide with the clicks marked, the cue to
come in on, who takes over next, a timer; ◀ ▶ or the arrow keys move the presentation.

    <address>/Apresentador              everyone's lines (the buttons at the top pick one person)
    <address>/Apresentador?quem=Lucas   opens on Lucas's lines: each presenter can keep their own link

On a phone or in another browser the page cannot reach the presentation (browsers only talk between tabs of the same
browser); ◀ ▶ then turn the script's own pages, so it still works as a script to read along.
The script PDFs (roteiro-*.pdf, copied next to app.py) appear as downloads in the bar at the top.
"""
import json
import re
import unicodedata
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "deck.html"

st.set_page_config(page_title="Apresentador", page_icon="▶", layout="wide", initial_sidebar_state="collapsed")


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "pessoa"


if not DECK.exists():
    st.error("deck.html não encontrado ao lado de app.py. Gere com build_deck.py e copie para cá.")
    st.stop()

html = DECK.read_text(encoding="utf-8")
m = re.search(r'<div class="deck"[^>]*\sdata-speakers="([^"]*)"', html)
roster = [x.strip() for x in (m.group(1).split("|") if m else []) if x.strip()]
asked = str(st.query_params.get("quem", "")).strip().lower()
quem = next((r for r in roster if r.lower() == asked or slug(r) == slug(asked)), "") if asked else ""   # only a name the deck declares
pdfs = sorted(ROOT.glob("roteiro*.pdf"), key=lambda f: (f.stem == "roteiro-geral", [f"roteiro-{slug(r)}" for r in roster].index(f.stem) if f.stem in [f"roteiro-{slug(r)}" for r in roster] else 99, f.name))   # the people in the deck's order, everyone last
BAR = 56 if pdfs else 0

st.markdown(
    f"""
    <style>
      header, footer, #MainMenu,
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], [data-testid="stSidebar"], [data-testid="collapsedControl"],
      [data-testid="stSidebarCollapsedControl"], [data-testid="stAppDeployButton"], .stDeployButton {{ display: none !important; }}
      html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{ background: #111 !important; overflow: hidden !important; }}
      .block-container, [data-testid="stMainBlockContainer"] {{ padding: 0 !important; max-width: 100% !important; }}
      [data-testid="stHorizontalBlock"] {{
        position: fixed; top: 0; left: 0; right: 0; height: {BAR}px; z-index: 999991; margin: 0 !important;
        padding: 0 16px; gap: 8px !important; align-items: center; background: #111; border-bottom: 1px solid #444;
      }}
      [data-testid="stHorizontalBlock"] > div {{ width: auto !important; flex: 0 0 auto !important; min-width: 0 !important; }}
      [data-testid="stHorizontalBlock"] > div:first-child [data-testid="stMarkdownContainer"],
      [data-testid="stHorizontalBlock"] > div:first-child [data-testid="stMarkdownContainer"] * {{
        margin: 0 6px 0 0 !important; padding: 0 !important; color: #bbb !important; font: 600 14px/30px system-ui, sans-serif !important; letter-spacing: .04em; }}
      .stDownloadButton button {{
        border-radius: 0 !important; background: none !important; color: #fff !important; border: 2px solid #777 !important;
        padding: 6px 12px !important; min-height: 0 !important; font: 600 14px/1 system-ui, sans-serif !important;
      }}
      .stDownloadButton button * {{ font: 600 14px/1 system-ui, sans-serif !important; margin: 0 !important; }}
      .stDownloadButton button:hover {{ border-color: #fff !important; }}
      iframe {{
        position: fixed !important; top: {BAR}px !important; left: 0 !important; z-index: 999990;
        width: 100vw !important; height: calc(100vh - {BAR}px) !important; height: calc(100dvh - {BAR}px) !important; border: 0 !important;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

if pdfs:
    names = {f"roteiro-{slug(r)}": r for r in roster}
    cols = st.columns(len(pdfs) + 1)
    cols[0].markdown("Roteiro em PDF")
    for c, f in zip(cols[1:], pdfs):
        label = names.get(f.stem) or ("Todos" if f.stem == "roteiro-geral" else "Roteiro")
        c.download_button(label, f.read_bytes(), file_name=f.name, mime="application/pdf", key=f.name)

# the engine opens in console mode when window.DECK_CONSOLE is set before it runs (a name, or "" for everyone)
inject = "<script>window.DECK_CONSOLE = " + json.dumps(quem).replace("<", "\\u003c") + ";</script>"
html, n = re.subn(r"<head\b[^>]*>", lambda mm: mm.group(0) + inject, html, count=1, flags=re.I)
if not n:
    html = inject + html

if hasattr(st, "iframe"):          # current API: an HTML string is embedded as it is, same-origin with the app
    st.iframe(html, height=800)
else:                              # older Streamlit
    import streamlit.components.v1 as components

    components.html(html, height=800, scrolling=False)
