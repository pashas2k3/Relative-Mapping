import boto3

if __name__ == '__main__':

    # This package works at userId level
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000", region_name='us-west-2')

    # Enter the userId for multiple different user
