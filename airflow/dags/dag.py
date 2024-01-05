from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from plugins.kaggle_operator import KaggleOperator
from datetime import datetime, timedelta
from includes.prepare_data import prepare_data
from includes.train_model import train_model
from includes.evaluate_model import evaluate_model

# определяем параметры рабочего процесса
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 31),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# создаем объект рабочего процесса
dag = DAG(
    'medical_cost_dag',
    default_args=default_args,
    description='A simple DAG to load, prepare, train and evaluate a dataset',
    schedule_interval='@daily',
)

# создаем задачи
load_data = KaggleOperator(
    task_id='load_data',
    dag=dag,
    dataset='code/theoneandonlyp/medical-cost-personal-datasets',
    output='/data/insurance.csv',
)

prepare_data = PythonOperator(
    task_id='prepare_data',
    dag=dag,
    python_callable=prepare_data,
    op_kwargs={'input_file': '/data/insurance.csv', 'output_file': '/data/insurance_prepared.csv'},
)

train_model = PythonOperator(
    task_id='train_model',
    dag=dag,
    python_callable=train_model,
    op_kwargs={'input_file': '/data/insurance_prepared.csv', 'output_file': '/data/insurance_model.joblib'},
)

evaluate_model = PythonOperator(
    task_id='evaluate_model',
    dag=dag,
    python_callable=evaluate_model,
    op_kwargs={'model_file': '/data/insurance_model.joblib', 'test_file': '/data/insurance_prepared.csv'},
)

# устанавливаем порядок выполнения задач
load_data >> prepare_data >> train_model >> evaluate_model
