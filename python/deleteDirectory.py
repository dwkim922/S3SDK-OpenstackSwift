import boto3

session = boto3.session.Session(profile_name='')

s3_client = session.client(
    service_name='s3',
    region_name='us-east-1',
    endpoint_url='',
)

prefix = ''  # folder name
bucket = ''  # bucket name

objects = s3_client.list_objects(Bucket=bucket, Prefix=prefix)

for obj in objects.get('Contents', []):
    s3_client.delete_object(Bucket=bucket, Key=obj['Key'])
