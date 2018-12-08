'''
Test E2E with DynamoDB local
'''

import boto3


if __name__ == '__main__'
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000", region_name='us-west-2')