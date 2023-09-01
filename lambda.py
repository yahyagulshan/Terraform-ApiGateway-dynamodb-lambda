import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ExampleDynamoDB')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']

    response = table.get_item(Key={'username': username})

    if 'Item' in response:
        stored_password = response['Item']['password']
        if stored_password == password:
            return {
                "statusCode": 200,
                "body": json.dumps("Login successful")
            }

    return {
        "statusCode": 401,
        "body": json.dumps("Username or password is incorrect")
    }
