import pandas as pd

def load_data():
    return pd.read_csv("pipeline_data.csv")


def compute_metrics(df):
    summary = df.groupby("team").agg(
        avg_duration=("duration_sec", "mean"),
        max_duration=("duration_sec", "max"),
        min_duration=("duration_sec", "min"),
        success_rate=("status", lambda x: (x == "SUCCESS").mean())
    ).reset_index()

    return summary


def find_fastest_team(summary):
    fastest = summary.loc[summary["avg_duration"].idxmin()]
    return fastest["team"], fastest["avg_duration"]


def find_slowest_team(summary):
    slowest = summary.loc[summary["avg_duration"].idxmax()]
    return slowest["team"], slowest["avg_duration"]


def detect_instability(df):
    instability = df.groupby("team")["duration_sec"].std().reset_index()
    instability.columns = ["team", "std_dev"]

    most_unstable = instability.loc[instability["std_dev"].idxmax()]
    return most_unstable["team"], most_unstable["std_dev"]


def generate_insights(summary, df):
    fastest_team, fastest_time = find_fastest_team(summary)
    slowest_team, slowest_time = find_slowest_team(summary)
    unstable_team, std_dev = detect_instability(df)

    insights = []

    insights.append(f"🚀 Fastest pipeline: {fastest_team} ({fastest_time:.2f} sec avg)")
    insights.append(f"🐢 Slowest pipeline: {slowest_team} ({slowest_time:.2f} sec avg)")
    insights.append(f"⚠️ Most unstable pipeline: {unstable_team} (std dev {std_dev:.2f})")

    return insights


if __name__ == "__main__":
    df = load_data()

    summary = compute_metrics(df)
    insights = generate_insights(summary, df)

    print("\n📊 PIPELINE METRICS:\n")
    print(summary)

    print("\n🧠 INSIGHTS:\n")
    for insight in insights:
        print("-", insight)