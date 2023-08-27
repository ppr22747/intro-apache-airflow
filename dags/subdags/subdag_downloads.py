from airflow import DAG
from airflow.operators.bash import BashOperator

def subdag_downloads(parent_dag_id, child_dag_id, args):

    with DAG(f"{parent_dag_id}.{child_dag_id}",
        start_date=args['start_date'],
        schedule_interval=args['schedule_interval'],
        catchup=args['catchup']) as dag:

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
        return dag