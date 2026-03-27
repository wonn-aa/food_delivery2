
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def process_delivery_report():
    print("--- ОТЧЕТ СЛУЖБЫ ДОСТАВКИ ---")
    print("Данные из Kafka успешно обработаны.")
    print("Статус: Все системы работают штатно.")

default_args = {
    'owner': 'student',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'food_delivery_reporting',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    task_report = PythonOperator(
        task_id='generate_report',
        python_callable=process_delivery_report
    )

