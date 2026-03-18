# Design Document – Pipeline Performance Benchmarker

## 1. Introduction

This project is designed to benchmark the performance of CI/CD pipelines across different teams using Jenkins.  
It collects pipeline execution data, analyzes performance metrics, and presents insights through a dashboard.

---

## 2. System Architecture

The system follows a simple data pipeline architecture:

Jenkins Pipelines → Jenkins API → Data Collector → Metrics Engine → Dashboard

---

## 3. Components

### 3.1 Jenkins Pipelines
- Simulated pipelines for multiple teams  
- Each pipeline consists of stages: Build, Test, Deploy  
- Pipelines generate execution data (duration, status)

---

### 3.2 Data Collector
- Implemented in Python  
- Fetches pipeline data using Jenkins REST API  
- Extracts:
  - build number  
  - execution status  
  - duration  

- Stores data in CSV format

---

### 3.3 Metrics Engine
- Processes collected data using Pandas  
- Computes:
  - average duration  
  - minimum and maximum duration  
  - success rate  

- Performs analysis:
  - fastest and slowest pipelines  
  - performance gap  
  - stability (standard deviation)  
  - outlier detection  

---

### 3.4 Dashboard
- Built using Streamlit  
- Displays:
  - pipeline comparison charts  
  - ranking of teams  
  - performance insights  

- Provides interactive visualization of benchmarking results

---

## 4. Data Flow

1. Pipelines are executed in Jenkins  
2. Data is fetched using Jenkins API  
3. Data is stored in CSV  
4. Metrics are computed from the dataset  
5. Dashboard visualizes results  

---

## 5. Key Design Decisions

### Use of Jenkins API
Chosen to directly access real pipeline execution data.

### Use of Pandas
Efficient for data processing and aggregation.

### Use of Streamlit
Provides quick and interactive visualization without complex frontend development.

---

## 6. Assumptions

- Jenkins is running locally  
- Pipelines are executed multiple times to generate sufficient data  
- All pipelines follow a similar structure  

---

## 7. Limitations

- Uses simulated pipelines (not production workloads)  
- Limited to small dataset (last few builds)  
- No real-time streaming of pipeline data  

---

## 8. Future Enhancements

- Real-time data monitoring  
- Integration with multiple CI tools  
- Advanced anomaly detection  
- Historical trend analysis  

---