import boto3
from src.dot_env.domain.aws import AWS

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS.access_key_id,
    aws_secret_access_key=AWS.secret_access_key
)
