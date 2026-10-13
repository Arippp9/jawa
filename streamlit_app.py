
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="UV-1700 PharmaSpec 3D",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #faf9f5;
}
.block-container {
    max-width: 1100px;
    padding-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🔬 Shimadzu UV-1700 PharmaSpec")
st.caption(
    "Model 3D interaktif spektrofotometer UV-Vis. "
    "Putar model, amati bagian luar dan dalam, "
    "serta pelajari fungsi komponen."
)

html_path = Path(__file__).parent / "UV-1700 PharmaSpec 3D.html"

if html_path.exists():
    html_code = html_path.read_text(encoding="utf-8")
    components.html(
        html_code,
        height=760,
        scrolling=True
    )
else:
    st.error(
        "File uv1700.html tidak ditemukan. "
        "Pastikan file tersebut berada satu folder "
        "dengan streamlit_app.py di GitHub."
    )

st.divider()

st.markdown("""
<div style="text-align:center;color:#777;padding:12px">
<b>UV-Vis Explorer</b><br>
Laboratorium Virtual Spektrofotometri UV-Vis<br>
Media pembelajaran dan simulasi instrumen
</div>
""", unsafe_allow_html=True)
