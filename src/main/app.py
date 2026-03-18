import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pipeline Benchmarker", layout="wide")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("pipeline_data.csv")

# ---------------- TITLE ----------------
st.title("🚀 CI/CD Pipeline Performance Benchmarker")

st.markdown("Compare pipeline efficiency across teams using Jenkins data")

# ---------------- METRICS ----------------
summary = df.groupby("team").agg(
    avg_duration=("duration_sec", "mean"),
    success_rate=("status", lambda x: (x == "SUCCESS").mean())
).reset_index()

# ---------------- TOP METRICS ----------------
col1, col2, col3 = st.columns(3)

fastest_team = summary.loc[summary["avg_duration"].idxmin()]
slowest_team = summary.loc[summary["avg_duration"].idxmax()]

col1.metric("🚀 Fastest Pipeline", fastest_team["team"], f"{fastest_team['avg_duration']:.2f} sec")
col2.metric("🐢 Slowest Pipeline", slowest_team["team"], f"{slowest_team['avg_duration']:.2f} sec")
col3.metric("📊 Total Runs", len(df))

st.divider()

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Duration per Team")
    st.bar_chart(summary.set_index("team")["avg_duration"])

with col2:
    st.subheader("✅ Success Rate")
    st.bar_chart(summary.set_index("team")["success_rate"])

# ---------------- RAW DATA ----------------
st.divider()
st.subheader("📄 Raw Pipeline Data")
st.dataframe(df)

# ---------------- INSIGHTS ----------------
st.divider()
st.subheader("🧠 Insights")

gap = slowest_team["avg_duration"] - fastest_team["avg_duration"]

st.write(f"🚀 Fastest pipeline: **{fastest_team['team']}**")
st.write(f"🐢 Slowest pipeline: **{slowest_team['team']}**")
st.write(f"📉 Performance gap: **{gap:.2f} seconds**")

# Instability
std_dev = df.groupby("team")["duration_sec"].std()
unstable_team = std_dev.idxmax()

st.write(f"⚠️ Most unstable pipeline: **{unstable_team}**")