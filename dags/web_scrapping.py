from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

default_args = {
    "owner": "ferry",
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="web_scrapping_dag",
    default_args=default_args,
    dagrun_timeout=timedelta(minutes=60),
    description="dag for web scrapping",
    start_date=days_ago(1)
) as dag:

    start = DummyOperator(task_id="start") 

    scrapping = BashOperator(
        task_id = "web_scrapping_task",
        bash_command="cd /opt/airflow/scripts && python scrapping.py",
    )

    end = DummyOperator(task_id="end")

    start >> scrapping >> end