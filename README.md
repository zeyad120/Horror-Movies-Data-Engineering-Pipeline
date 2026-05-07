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
http://localhost:8080
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
SELECT 
    COUNT(*) AS total_records,
    COUNT(DISTINCT id) AS unique_records
FROM fact_movies;
```

### ✔ Missing Values Check
```sql
SELECT *
FROM fact_movies
WHERE title IS NULL OR vote_average IS NULL;
```

### ✔ Rating Validation
```sql
SELECT *
FROM fact_movies
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
