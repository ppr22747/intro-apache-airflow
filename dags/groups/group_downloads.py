# from airflow import DAG
# from airflow.operators.bash import BashOperator

# def subdag_downloads(parent_dag_id, child_dag_id, args):

#     with DAG(f"{parent_dag_id}.{child_dag_id}",
#         start_date=args['start_date'],
#         schedule_interval=args['schedule_interval'],
#         catchup=args['catchup']) as dag:

#         downloads_a = BashOperator(
#             task_id='downloads_a',
#             bash_command='sleep 10'
#         )

#         downloads_b = BashOperator(
#             task_id='downloads_b',
#             bash_command='sleep 10'
#         )

#         downloads_c = BashOperator(
#             task_id='downloads_c',
#             bash_command='sleep 10'
#         )
#         return dag

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def download_tasks():

    with TaskGroup("downloads", tooltip="Downloads tasks") as group:

        downloads_a = BashOperator(
            task_id='downloads_a',
            bash_command='sleep 10'
        )

        downloads_b = BashOperator(
            task_id='downloads_b',
            bash_command='sleep 10'
        )

        downloads_c = BashOperator(
            task_id='downloads_c',
            bash_command='sleep 10'
        )
        return group