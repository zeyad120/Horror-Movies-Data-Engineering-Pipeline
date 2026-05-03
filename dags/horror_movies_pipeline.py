from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta
import os

# تحديد المسار الحالي للمشروع عشان نربط المجلدات صح
# ملاحظة: في ويندوز يفضل كتابة المسار كامل أو التأكد من إعدادات Docker Desktop
PROJECT_PATH = "D:/Me/sem-6/Data Mining and Big Data Analysis/Project/data-engineering-project"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'horror_movies_cleaning_pipeline',
    default_args=default_args,
    description='Pipeline to clean horror movies data using Spark',
    schedule_interval=None,  # هنشغله يدوي للتجربة
    catchup=False,
) as dag:

    clean_data_spark = DockerOperator(
        task_id='run_spark_cleaning',
        image='apache/spark:3.4.1',
        # نفس الأمر اللي جربناه في الـ PowerShell
        command='/opt/spark/bin/spark-submit /tmp/spark/clean_horror_data.py',
        api_version='auto',
        auto_remove=True,
        # ربط الفولدرات (Volumes) بنفس الطريقة
        volumes=[
            f'{PROJECT_PATH}/spark:/tmp/spark',
            f'{PROJECT_PATH}/data:/tmp/data'
        ],
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    clean_data_spark