import requests
import pandas as pd

JENKINS_URL = "http://localhost:8080"
PIPELINES = ["team-a-pipeline", "team-b-pipeline", "team-c-pipeline"]

USERNAME = "JunkYak"
API_TOKEN = "110e9ec2e938d4119981864bf5d4032722"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_build_data(pipeline_name):
    url = f"{JENKINS_URL}/job/{pipeline_name}/api/json"

    response = requests.get(url, headers=HEADERS, auth=(USERNAME, API_TOKEN))
    print(f"{pipeline_name} STATUS:", response.status_code)

    if response.status_code != 200:
        print(f" Failed to fetch {pipeline_name}")
        return []

    data = response.json()
    builds = data.get("builds", [])[:5]

    build_data_list = []

    for build in builds:
        build_url = build["url"] + "api/json"

        build_response = requests.get(build_url, headers=HEADERS, auth=(USERNAME, API_TOKEN))

        if build_response.status_code != 200:
            continue

        build_data = build_response.json()

        build_data_list.append({
            "team": pipeline_name,
            "build_number": build_data.get("number"),
            "status": build_data.get("result"),
            "duration_sec": build_data.get("duration", 0) / 1000
        })

    return build_data_list


def collect_all_data():
    all_data = []

    for pipeline in PIPELINES:
        print(f"\nFetching data for {pipeline}...")
        pipeline_data = fetch_build_data(pipeline)
        all_data.extend(pipeline_data)

    return pd.DataFrame(all_data)


if __name__ == "__main__":
    df = collect_all_data()

    if df.empty:
        print("\n No data collected!")
    else:
        df.to_csv("pipeline_data.csv", index=False)
        print("\n Data collected successfully!\n")
        print(df)