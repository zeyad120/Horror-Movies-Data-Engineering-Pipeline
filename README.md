📊 Horror Movies Data Engineering Pipeline
📌 Project Overview

This project is a complete Data Engineering pipeline built to process and analyze a horror movies dataset.
It demonstrates how to build an end-to-end workflow using Airflow, Docker, and data processing techniques to extract, transform, and validate data.

The pipeline automates data ingestion, cleaning, transformation, and orchestration of tasks to produce a final clean dataset ready for analysis.

⚙️ Tech Stack
Apache Airflow
Docker
Python (Pandas)
SQL / Data Warehousing concepts
Git & GitHub
🏗️ Project Architecture

The pipeline follows an ETL structure:

Extract
Load raw dataset (movies data)
Transform
Clean missing values
Normalize columns
Handle duplicates
Feature formatting (dates, genres, etc.)
Load
Store processed data in final output table / file
Orchestration
Airflow DAG manages all tasks in sequence
🔄 Airflow DAG Workflow

The DAG includes multiple tasks such as:

Data extraction task
Data cleaning task
Data transformation task
Validation task
Final load task

All tasks are executed in sequence using Airflow scheduling.

🚀 How to Run the Project
1. Start Docker
docker-compose up -d
2. Start Airflow UI

Open in browser:

http://localhost:8080
3. Trigger DAG
Go to Airflow dashboard
Enable DAG: multi_task_pipeline
Trigger manually or wait for schedule
📊 Final Output Validation

After execution:

Clean dataset is generated successfully
Data is validated for consistency and completeness
Logs confirm successful pipeline execution
📁 Project Structure
data-engineering-project/
│
├── dags/
│   └── multi_task_pipeline.py
├── data/
│   └── raw_dataset.csv
├── scripts/
│   └── transformations.py
├── docker-compose.yml
└── README.md
📌 Key Features
Fully automated ETL pipeline
Modular Airflow DAG design
Dockerized environment for easy deployment
Scalable structure for big data projects
Clean and validated output datase

👨‍💻 Author
Zeyad Elmogy

📎 Notes

This project was developed as part of a Data Engineering coursework project focusing on pipeline design, orchestration, and real-world data processing workflows.
