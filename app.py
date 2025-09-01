import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Baseline Demo", page_icon="✅", layout="centered")

st.title("Baseline — Streamlit Demo")
st.caption("A super simple app with inputs, a chart, and CSV preview.")

# --- Inputs ---
name = st.text_input("Your name", "World")
points = st.slider("How many points for the chart?", 50, 1000, 200, 50)

st.write(f"Hello, **{name}**! 👋")

# --- Simple chart ---
rng = np.random.default_rng(42)
x = np.arange(points)
y = rng.normal(0, 1, size=points).cumsum()
chart_df = pd.DataFrame({"x": x, "y": y})

st.subheader("Random Walk")
st.line_chart(chart_df, x="x", y="y")

# --- File upload & preview ---
st.subheader("Upload a CSV (optional)")
uploaded = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.success("Loaded!")
    st.dataframe(df.head(20), use_container_width=True)

# --- Little progress demo ---
if st.button("Do a quick task"):
    with st.spinner("Working..."):
        for i in range(1, 6):
            time.sleep(0.2)
            st.progress(i * 20, text=f"Step {i}/5")
    st.success("Done!")

with st.expander("Notes"):
    st.markdown(
        "- This app uses Streamlit's widgets, charts, and file uploader.\n"
        "- To run locally: `pip install streamlit && streamlit run app.py`.\n"
        "- On Community Cloud, just add a `requirements.txt` with `streamlit`."
    )
