# 📊 Horror Movies Data Engineering Pipeline

## 📌 Project Overview

This project is a complete Data Engineering pipeline built to process and analyze a horror movies dataset.  
It demonstrates an end-to-end workflow using **Apache Airflow**, **Docker**, and data processing techniques to extract, transform, and validate data.

The pipeline automates data ingestion, cleaning, transformation, and orchestration of tasks to produce a final clean dataset ready for analysis.

---

## ⚙️ Tech Stack

- Apache Airflow  
- Docker  
- Python (Pandas)  
- SQL / Data Warehousing concepts  
- Git & GitHub

---

## ⚡ Big Data Processing Layer (Spark + HDFS + YARN)

To simulate a real-world Big Data environment, the pipeline is designed to conceptually integrate the following technologies:

### 🔥 Apache Spark
Apache Spark is used for distributed data processing and transformation of the raw movies dataset.  
It handles large-scale data cleaning, aggregation, and feature engineering in a parallel computing environment.

Example operations:
- Data filtering and cleaning at scale
- Genre parsing and normalization
- Aggregations on ratings and votes

---

### 📦 HDFS (Hadoop Distributed File System)
HDFS is considered as the storage layer for raw and processed data in a distributed environment.

- Raw dataset is stored in HDFS
- Cleaned dataset is written back to HDFS
- Enables fault-tolerant and scalable storage

---

### ⚙️ YARN (Yet Another Resource Negotiator)
YARN is used as the cluster resource manager to:

- Allocate resources for Spark jobs
- Manage job scheduling and execution
- Ensure efficient distributed processing

---

### 🧠 Integration with Airflow
Airflow acts as the orchestration layer that triggers Spark jobs and manages the full pipeline workflow:

Airflow → Spark Jobs → HDFS Storage → Final Output

---

### 📌 Note
In this project, Spark, HDFS, and YARN are integrated at a conceptual / architectural level to demonstrate a real-world Big Data pipeline design.

---

## 🏗️ Project Architecture

The pipeline follows a standard ETL workflow:

- **Extract** → Load raw movies dataset  
- **Transform** → Clean missing values, normalize columns, handle duplicates, format features  
- **Load** → Store processed data into final output dataset  
- **Orchestration** → Airflow DAG manages and schedules all tasks  

---

## 🧱 Data Warehouse Schema

The project transforms the raw movies dataset into a simple data warehouse structure:

### 1. fact_movies
Main table containing movie details:
- id (Primary Key)  
- title  
- original_language  
- release_date  
- vote_count  
- vote_average  
- adult  
- status  

---

### 2. dim_genres
Dimension table containing unique genres:
- genre_id (Primary Key)  
- genre_name  

---

### 3. movie_genres_bridge
Bridge table to handle many-to-many relationship between movies and genres:
- movie_id (Foreign Key)  
- genre_id (Foreign Key)  

---

## 🔄 Airflow DAG Workflow

The pipeline includes the following tasks:

- Data extraction  
- Data cleaning  
- Data transformation  
- Data validation  
- Final data loading  

All tasks are executed sequentially using **Airflow DAG orchestration**.

---

## 🚀 How to Run the Project

### 1. Start Docker
```bash
docker-compose up -d
```

---

### 2. Start Airflow UI
Open in browser:

```
http://localhost:8081
```

---

### 3. Trigger DAG
- Open Airflow dashboard  
- Enable DAG: `multi_task_pipeline`  
- Trigger manually or wait for schedule  

---

## 📊 Final Output Validation

To ensure data quality and correctness, the following checks were performed:

### ✔ Total & Unique Records
```sql
SELECT COUNT(*) FROM fact_movie;
```

### ✔ Missing Values Check
```sql
SELECT *
FROM fact_movie
WHERE vote_average IS NULL OR vote_count IS NULL;
```

### ✔ Rating Validation
```sql
SELECT *
FROM fact_movie
WHERE vote_average < 0 OR vote_average > 10;
```

---

## 📁 Project Structure

```
data-engineering-project/
│
├── dags/
│   └── multi_task_pipeline.py
│
├── data/
│   └── raw_dataset.csv
│
├── scripts/
│   └── transformations.py
│
├── docker-compose.yml
│
└── README.md
```

---

## 📌 Key Features

- Fully automated ETL pipeline  
- Modular Airflow DAG design  
- Dockerized environment for easy deployment  
- Data validation layer  
- Clean and structured final dataset  

---

## 👨‍💻 Author

Zeyad Elmogy  

---

## 📎 Notes

This project was developed as part of a Data Engineering coursework assignment focusing on pipeline design, orchestration, and real-world data processing workflows.

<img width="1916" height="984" alt="Screenshot 2026-05-07 194817" src="https://github.com/user-attachments/assets/c3928ee5-4958-4c59-b1b9-a049ade32b84" />
<img width="1919" height="756" alt="Screenshot 2026-05-07 194807" src="https://github.com/user-attachments/assets/0fe93afa-ae14-4891-b4dd-27d9173c77ad" />
<img width="1919" height="1032" alt="Screenshot 2026-05-07 194747" src="https://github.com/user-attachments/assets/e15d2cc9-70d6-4b44-ac4b-e2014336e071" />

