import boto3
import yaml


def get_table(table):
    with open('credentials.yml', 'r') as f:
        credentials = yaml.safe_load(f)
    session = boto3.Session(aws_access_key_id=credentials['aws_access_key_id'],
                            aws_secret_access_key=credentials['aws_secret_access_key'],
                            aws_session_token=credentials['aws_session_token'],
                            region_name=credentials['region_name'])

    dynamodb = session.resource('dynamodb')
    return dynamodb.Table(table)
