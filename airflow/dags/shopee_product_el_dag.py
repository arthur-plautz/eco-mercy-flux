import os
import json

from datetime import timedelta, date
from textwrap import dedent

from airflow import DAG

from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago

from airflow.dags.variables import *

default_email = 'atr.plautz@gmail.com'
tags = 'shopee'
target_file = "{{ ds }}".replace('-','_')

crawler_config = {
    'run': crawler_operation,
    'model': crawler_model,
    'search': crawler_search,
    'filters': crawler_filters,
    's3_bucket': target_bucket,
    'output': target_file
}

embulk_plugins = 'embulk-input-s3 embulk-output-postgresql embulk-filter-add_time'
embulk_config = {
    'in': {
        'type': 's3',
        'bucket': target_bucket,
        'path_prefix': f'data/{operation}/{search}/e{target_file}.csv',
        'endpoint': f's3.{region}.amazonaws.com',
        'access_key_id': aws_public,
        'secret_access_key': aws_secret
    },
    'filters': [{
        'type': 'add_time',
        'to_column': {
            'name': 'extraction_date',
            'type': 'timestamp'
        }
    }],
    'out': {
        'type': 'postgresql',
        'host': db_host,
        'user': db_user,
        'port': db_port,
        'password': db_pass,
        'database': db_name,
        'table': db_table,
        'mode': 'insert_direct'
    }
}

default_args = {
    'owner': 'arthur-plautz',
    'depends_on_past': False,
    'email': [default_email],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
with DAG(
    'shopee_el',
    default_args=default_args,
    description='Shopee EL Flux',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=[tags],
) as dag:

    crawler = DockerOperator(
        task_id='crawler_data_extraction',
        image='arthurplautz/eco-mercy-scrapers:0.1',
        network_mode="bridge",
        do_xcom_push=False,
        api_version='auto',
        auto_remove=True,
        environment={
            'AF_EXECUTION_DATE': "{{ ds }}",
            'AF_OWNER': "{{ task.owner }}",
            'CONFIG': json.dumps(crawler_config),
            'AWS_PUBLIC': aws_public,
            'AWS_SECRET': aws_secret
        }
    )

    embulk = DockerOperator(
        task_id='crawler_data_load',
        image='arthurplautz/general-embulk:0.1',
        network_mode="bridge",
        api_version='auto',
        do_xcom_push=False,
        auto_remove=True,
        environment={
            'AF_EXECUTION_DATE': "{{ ds }}",
            'AF_OWNER': "{{ task.owner }}",
            'PLUGINS': embulk_plugins,
            'CONFIG': json.dumps(embulk_config),
            'AWS_PUBLIC': aws_public,
            'AWS_SECRET': aws_secret
        }
    )

    crawler >> embulk