import boto3

session = boto3.session.Session(profile_name='zadara')

s3_client = session.client(
    service_name='s3',
    region_name='us-east-1',
    endpoint_url='',
)

objectName = 'test.txt'
bucket = 'tempurl'

response = s3_client.upload_file(
    objectName, bucket, objectName,
    ExtraArgs={'ContentType': 'abc/test'}
     )
