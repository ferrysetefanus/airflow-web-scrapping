from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    "owner": "ferry",
    "retry_delay": timedelta(minutes=5),
}

web_scrapping_dag = DAG(
    dag_id="web_scrapping_dag",
    default_args=default_args,
    dagrun_timeout=timedelta(minutes=60),
    description="dag for web scrapping",
    start_date=days_ago(1)
)

