import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pipeline Performance Benchmarker", layout="wide")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("pipeline_data.csv")

# ---------------- HEADER ----------------
st.title("CI/CD Pipeline Performance Benchmarker")
st.markdown("Real-time CI/CD Pipeline Performance Benchmarker")

st.divider()

# ---------------- STUDENT INFO ----------------
with st.expander("Project Information", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Student Name:** Priya Agrawal")
        st.markdown("**Course:** IIS3250 DevOps")
    with col2:
        st.markdown("**Project Tool:** Jenkins & CI/CD")
        st.markdown("**Semester:** VI")

st.divider()

# ---------------- SUMMARY METRICS ----------------
summary = df.groupby("team").agg(
    avg_duration=("duration_sec", "mean"),
    success_rate=("status", lambda x: (x == "SUCCESS").mean())
).reset_index()

fastest = summary.loc[summary["avg_duration"].idxmin()]
slowest = summary.loc[summary["avg_duration"].idxmax()]

# ---------------- TOP METRICS ----------------
st.subheader("Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Fastest Pipeline", fastest["team"], f"{fastest['avg_duration']:.2f} sec")
col2.metric("Slowest Pipeline", slowest["team"], f"{slowest['avg_duration']:.2f} sec")
col3.metric("Total Runs", len(df))

st.divider()

# ---------------- CHARTS ----------------
st.subheader("Performance Charts")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Average Duration per Team (seconds)**")
    st.bar_chart(summary.set_index("team")["avg_duration"])

with col2:
    st.markdown("**Success Rate per Team**")
    st.bar_chart(summary.set_index("team")["success_rate"])

st.divider()

# ---------------- RANKING ----------------
st.subheader("Pipeline Ranking (Fastest to Slowest)")
ranking = summary.sort_values("avg_duration").reset_index(drop=True)
ranking.index += 1
st.dataframe(ranking, width='stretch')

# ---------------- PERFORMANCE GAP ----------------
gap = slowest["avg_duration"] - fastest["avg_duration"]
st.info(f"Performance gap between fastest and slowest pipeline: {gap:.2f} seconds")

st.divider()

# ---------------- STABILITY ----------------
st.subheader("Pipeline Stability (Standard Deviation)")
st.markdown("Lower standard deviation means more consistent and stable pipeline runs.")
std_dev = df.groupby("team")["duration_sec"].std().reset_index()
std_dev.columns = ["team", "std_deviation"]
st.bar_chart(std_dev.set_index("team")["std_deviation"])

unstable_team = std_dev.loc[std_dev["std_deviation"].idxmax(), "team"]
st.warning(f"Most unstable pipeline: {unstable_team}")

st.divider()

# ---------------- OUTLIERS ----------------
st.subheader("Outlier Runs")
st.markdown("Runs that took more than 1.5x the average duration are flagged as outliers.")
threshold = df["duration_sec"].mean() * 1.5
outliers = df[df["duration_sec"] > threshold]

if outliers.empty:
    st.success("No significant outliers detected.")
else:
    st.dataframe(outliers, width='stretch')

st.divider()

# ---------------- RAW DATA ----------------
st.subheader("Raw Pipeline Data")
st.dataframe(df, width='stretch')