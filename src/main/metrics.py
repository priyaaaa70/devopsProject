import pandas as pd

# ---------------- LOAD DATA ----------------
def load_data():
    return pd.read_csv("pipeline_data.csv")


# ---------------- METRICS ----------------
def compute_metrics(df):
    summary = df.groupby("team").agg(
        avg_duration=("duration_sec", "mean"),
        max_duration=("duration_sec", "max"),
        min_duration=("duration_sec", "min"),
        success_rate=("status", lambda x: (x == "SUCCESS").mean())
    ).reset_index()

    return summary


# ---------------- ANALYSIS ----------------
def find_fastest_team(summary):
    row = summary.loc[summary["avg_duration"].idxmin()]
    return row["team"], row["avg_duration"]


def find_slowest_team(summary):
    row = summary.loc[summary["avg_duration"].idxmax()]
    return row["team"], row["avg_duration"]


def detect_instability(df):
    std_dev = df.groupby("team")["duration_sec"].std()
    unstable_team = std_dev.idxmax()
    return unstable_team, std_dev


def detect_outliers(df):
    threshold = df["duration_sec"].mean() * 1.5
    outliers = df[df["duration_sec"] > threshold]
    return outliers


# ---------------- INSIGHTS ----------------
def generate_insights(summary, df):
    fastest_team, fastest_time = find_fastest_team(summary)
    slowest_team, slowest_time = find_slowest_team(summary)
    unstable_team, std_dev = detect_instability(df)
    outliers = detect_outliers(df)

    insights = []

    # Core insights
    insights.append(f"Fastest pipeline: {fastest_team} ({fastest_time:.2f} sec avg)")
    insights.append(f"Slowest pipeline: {slowest_team} ({slowest_time:.2f} sec avg)")

    # Performance gap
    gap = slowest_time - fastest_time
    insights.append(f"Performance gap: {gap:.2f} seconds between fastest and slowest")

    # Stability
    insights.append(f"Most unstable pipeline: {unstable_team} (std dev {std_dev[unstable_team]:.2f})")

    # Ranking
    ranking = summary.sort_values("avg_duration")
    insights.append("\nRanking (Fastest → Slowest):")
    for i, row in enumerate(ranking.itertuples(), 1):
        insights.append(f"{i}. {row.team} ({row.avg_duration:.2f} sec)")

    return insights, std_dev, outliers


# ---------------- MAIN ----------------
if __name__ == "__main__":
    df = load_data()

    summary = compute_metrics(df)
    insights, std_dev, outliers = generate_insights(summary, df)

    print("\nPIPELINE METRICS:\n")
    print(summary)

    print("\nINSIGHTS:\n")
    for insight in insights:
        print("-", insight)

    print("\nSTABILITY (STD DEV):\n")
    print(std_dev)

    print("\nOUTLIER RUNS:\n")
    print(outliers if not outliers.empty else "No significant outliers")