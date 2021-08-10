from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from dag_utils.gcs_utils import list_blobs

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    dag_id='test_gcs',
    start_date=days_ago(2),
    schedule_interval=None,
    tags=['gcloud'],
    default_args=default_args,
)

list_blobs = PythonOperator(
    task_id='list_blobs',
    python_callable=list_blobs,
    op_args=['airflow-k8s-test'],
    dag=dag
)

list_blobs
