# Pipeline Performance Benchmarker

**Student Name:** Ishan Anand  
**Registration No:** 23FE10CSE00311  
**Course:** CSE3253 DevOps [PE6]  
**Semester:** VI (2025–2026)  
**Project Tool:** Jenkins & CI  
  

---

## 📌 Project Overview

### Problem Statement
In modern CI/CD workflows, multiple teams run pipelines, but there is limited visibility into how efficiently these pipelines perform.  
This makes it difficult to identify slow pipelines, inconsistencies, and performance bottlenecks.

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

## 🛠️ Technology Stack

### Core Technologies
- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Data Processing:** Pandas  

### DevOps Tools
- **CI/CD:** Jenkins  
- **Version Control:** Git  

---

## ⚙️ How It Works

1. Jenkins pipelines are executed for multiple teams  
2. Pipeline data is fetched using Jenkins API  
3. Metrics are computed (duration, success rate, variability)  
4. Insights are generated  
5. Results are visualized in a dashboard  

---

## 📊 Performance Metrics

- Average Pipeline Duration  
- Success Rate  
- Performance Gap (Fastest vs Slowest)  
- Stability (Standard Deviation)  
- Outlier Detection  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+  
- Jenkins running locally  

---

### Installation

1. Clone the repository:
```bash
git clone https://github.com/JunkYak/devopsProject
cd devopsprojectpipelinebenchmarker
