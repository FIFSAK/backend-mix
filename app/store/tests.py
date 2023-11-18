from django.test import TestCase

# Create your tests here.
import boto3
from botocore.exceptions import NoCredentialsError

try:
    s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='YOUR_SECRET_KEY')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f'Bucket Name: {bucket["Name"]}')
except NoCredentialsError:
    print("Credentials not available")

