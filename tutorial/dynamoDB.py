import boto3
def get_table(table):

    session = boto3.Session(aws_access_key_id='ASIA3HDTN5VX37WIPATL',
                            aws_secret_access_key='ot82okQ1iFjeC+Y89MzW9G+LRWJYyg2lfmXTdkaV',
                            aws_session_token='FwoGZXIvYXdzENP//////////wEaDDeV/wgIZA127HPxJiK/AVHEKvbpy8MpZrMy1zKqjjhEvuVv1AMUa7M5HmnZYCWo+5FBE7VUKz+9SCPkfobgMAnC/Z8FpThkGIh/TqK/PswehUP3xsDs38t/CAjT3fnAQA6TOLQWvtuhPM4HKFrxwcpYIK7BnKqeOPEHy4igx9lHzPkqLU3AXaHwQ+XsRrJFZBX9enNJmhhnq/HCeaGEtsiBsybQFs7r5efJdbBAvH5Q/CFB1ZR9ODYhy475myk1Ughq8yCVEpK0VeNepAj3KKjV8vAFMi3o9l5mVirxONiwCFChclMLW0vyNhkxnqFsG9z5EvTkhrIjAXBN3mShH8lz4+8=',
                            region_name='us-east-1')

    dynamodb = session.resource('dynamodb')
    return dynamodb.Table(table)    