# Pipeline Performance Benchmarker

**Student Name:** Priya Agrawal
**Registration No:** 23FE10CII00029
**Course:** IIS3250 DevOps 
**Semester:** VI 
**Project Tool:** Jenkins & CI

---

## Project Overview

### Problem Statement

In modern CI/CD workflows, multiple teams run pipelines, but there is limited visibility into how efficiently these pipelines perform. This makes it difficult to identify slow pipelines, inconsistencies, and performance bottlenecks.

---

### Objective

- Collect pipeline execution data from Jenkins
- Benchmark performance across teams
- Identify inefficiencies and variability
- Visualize insights using a dashboard

---

### Key Features

- Jenkins pipeline data collection via API
- Performance benchmarking across teams
- Insight generation (fastest, slowest, stability, outliers)
- Interactive dashboard using Streamlit

---

## Technology Stack

### Core Technologies

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard framework |
| Pandas | Data processing and analysis |
| Requests | Jenkins API communication |

### DevOps Tools

| Tool | Purpose |
|---|---|
| Jenkins | CI/CD pipeline execution |
| Git | Version control |
| GitHub | Remote repository hosting |

---

## Project Structure

```
devopsProject/
├── src/
│   └── main/
│       ├── app.py              # Streamlit dashboard UI
│       ├── collector.py        # Jenkins API data collector
│       └── metrics.py          # Performance metrics calculator
├── pipelines/
│   └── Jenkinsfile             # Jenkins pipeline definition
├── doc/
│   └── designdocument.md       # Project design document
├── pipeline_data.csv           # Collected pipeline data
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## How It Works

1. Jenkins pipelines are executed for multiple teams
2. Pipeline data is fetched using the Jenkins REST API
3. Metrics are computed (duration, success rate, variability)
4. Insights are generated (fastest, slowest, outliers, stability)
5. Results are visualized in an interactive Streamlit dashboard

---

## Performance Metrics

| Metric | Description |
|---|---|
| Average Pipeline Duration | Mean build time per team |
| Success Rate | Percentage of successful builds |
| Performance Gap | Difference between fastest and slowest team |
| Stability | Standard deviation of build durations |
| Outlier Detection | Runs exceeding 1.5x average duration |

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Jenkins running locally on port 8080
- Git installed

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/priyaaaa70/devopsProject.git
cd devopsProject
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure Jenkins credentials in `src/main/collector.py`:

```python
JENKINS_URL = "http://localhost:8080"
USERNAME = "your-jenkins-username"
API_TOKEN = "your-jenkins-api-token"
```

4. Collect pipeline data from Jenkins:

```bash
python src/main/collector.py
```

5. Launch the dashboard:

```bash
streamlit run src/main/app.py
```

6. Open your browser and go to:

```
http://localhost:8501
```

---

## Jenkins Setup

### Step 1 - Install Jenkins

Download and install Jenkins from https://www.jenkins.io/download/

### Step 2 - Create Pipeline Jobs

Create three pipeline jobs in Jenkins with the following names:

- `team-a-pipeline`
- `team-b-pipeline`
- `team-c-pipeline`

### Step 3 - Add Pipeline Script

Use the following Groovy script for each job (adjust sleep values per team):

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sleep 5
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sleep 3
            }
        }
    }
}
```

### Step 4 - Generate API Token

1. Click your username in Jenkins (top right)
2. Go to Security
3. Click Add new Token
4. Copy and save the token
5. Update `collector.py` with your credentials

### Step 5 - Run Each Pipeline

Click Build Now at least 3 times on each pipeline to generate build history.

---

## CI/CD Flow

1. Code is written and edited in VS Code
2. Changes are committed and pushed to GitHub
3. Jenkins detects the push via webhook
4. Jenkins automatically triggers the pipeline
5. Pipeline runs Build and Test stages
6. Stage view shows real-time progress
7. Dashboard is updated with the latest metrics

---

## Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt
```

| Package | Version | Purpose |
|---|---|---|
| streamlit | latest | Dashboard UI |
| pandas | latest | Data processing |
| requests | latest | API calls |

---

## Author

**Priya Agrawal**
Registration No: 23FE10CII00029
Course: IIS3250 DevOps 
Semester VI 