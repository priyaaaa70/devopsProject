import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pipeline Benchmarker", layout="wide")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("pipeline_data.csv")

# ---------------- TITLE ----------------
st.title("🚀 CI/CD Pipeline Performance Benchmarker")
st.markdown("Analyze and compare Jenkins pipeline performance across teams")

# ---------------- SUMMARY METRICS ----------------
summary = df.groupby("team").agg(
    avg_duration=("duration_sec", "mean"),
    success_rate=("status", lambda x: (x == "SUCCESS").mean())
).reset_index()

fastest = summary.loc[summary["avg_duration"].idxmin()]
slowest = summary.loc[summary["avg_duration"].idxmax()]

# ---------------- TOP METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("🚀 Fastest Pipeline", fastest["team"], f"{fastest['avg_duration']:.2f} sec")
col2.metric("🐢 Slowest Pipeline", slowest["team"], f"{slowest['avg_duration']:.2f} sec")
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

st.divider()

# ---------------- RANKING ----------------
st.subheader("🏆 Pipeline Ranking (Fastest → Slowest)")
ranking = summary.sort_values("avg_duration")
st.dataframe(ranking)

# ---------------- PERFORMANCE GAP ----------------
gap = slowest["avg_duration"] - fastest["avg_duration"]
st.info(f"📉 Performance gap between fastest and slowest: {gap:.2f} seconds")

# ---------------- STABILITY ----------------
st.subheader("📊 Pipeline Stability (Std Deviation)")
std_dev = df.groupby("team")["duration_sec"].std()
st.bar_chart(std_dev)

unstable_team = std_dev.idxmax()
st.warning(f"⚠️ Most unstable pipeline: {unstable_team}")

# ---------------- OUTLIERS ----------------
st.subheader("⚠️ Outlier Runs")
threshold = df["duration_sec"].mean() * 1.5
outliers = df[df["duration_sec"] > threshold]

if outliers.empty:
    st.success("No significant outliers detected")
else:
    st.dataframe(outliers)

# ---------------- RAW DATA ----------------
st.divider()
st.subheader("📄 Raw Pipeline Data")
st.dataframe(df)