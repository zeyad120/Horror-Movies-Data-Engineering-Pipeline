from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta

PROJECT_PATH = "D:/Me/sem-6/Data Mining and Big Data Analysis/Project/data-engineering-project"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='horror_movies_cleaning_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    description='Pipeline to clean horror movies data using Spark',
) as dag:

    extract_task = DockerOperator(
        task_id='extract_data',
        image='apache/spark:3.4.1',
        command='/opt/spark/bin/spark-submit /tmp/spark/extract_data.py',
        api_version='auto',
        auto_remove=True,
        volumes=[
            f'{PROJECT_PATH}/spark:/tmp/spark',
            f'{PROJECT_PATH}/data:/tmp/data'
        ],
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    nulls_task = DockerOperator(
        task_id='clean_nulls',
        image='apache/spark:3.4.1',
        command='/opt/spark/bin/spark-submit /tmp/spark/clean_nulls.py',
        api_version='auto',
        auto_remove=True,
        volumes=[
            f'{PROJECT_PATH}/spark:/tmp/spark',
            f'{PROJECT_PATH}/data:/tmp/data'
        ],
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    duplicates_task = DockerOperator(
        task_id='remove_duplicates',
        image='apache/spark:3.4.1',
        command='/opt/spark/bin/spark-submit /tmp/spark/remove_duplicates.py',
        api_version='auto',
        auto_remove=True,
        volumes=[
            f'{PROJECT_PATH}/spark:/tmp/spark',
            f'{PROJECT_PATH}/data:/tmp/data'
        ],
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    format_task = DockerOperator(
        task_id='format_columns',
        image='apache/spark:3.4.1',
        command='/opt/spark/bin/spark-submit /tmp/spark/format_columns.py',
        api_version='auto',
        auto_remove=True,
        volumes=[
            f'{PROJECT_PATH}/spark:/tmp/spark',
            f'{PROJECT_PATH}/data:/tmp/data'
        ],
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    save_task = DockerOperator(
        task_id='save_output',
        image='apache/spark:3.4.1',
        command='/opt/spark/bin/spark-submit /tmp/spark/save_output.py',
        api_version='auto',
        auto_remove=True,
        volumes=[
            f'{PROJECT_PATH}/spark:/tmp/spark',
            f'{PROJECT_PATH}/data:/tmp/data'
        ],
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    # ترتيب الـ pipeline
    extract_task >> nulls_task >> duplicates_task >> format_task >> save_task