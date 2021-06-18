from airflow.models import Variable

region = Variable.get('region')
aws_public = Variable.get('aws_public')
aws_secret = Variable.get('aws_secret')
target_bucket = Variable.get('target_bucket')
operation = Variable.get('operation')
search = Variable.get('search')

db_host = Variable.get('db_host')
db_port = Variable.get('db_port')
db_user = Variable.get('db_user')
db_pass = Variable.get('db_pass')
db_name = Variable.get('db_name')
db_table = Variable.get('db_table')

crawler_operation = Variable.get('crawler_operation')
crawler_model = Variable.get('crawler_model')
crawler_search = Variable.get('crawler_search')
crawler_filters = Variable.get('crawler_filters')