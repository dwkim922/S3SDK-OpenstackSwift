import boto3

session = boto3.session.Session(profile_name='zadara')

s3_client = session.client(
    service_name='s3',
    region_name='us-east-1',
    endpoint_url='https://vsa-00000004-kt-g-object-01.zadarazios.com',
)

objectName = 'test.txt'
bucket = 'tempurl'

s3_client.delete_object(Bucket = bucket, Key = objectName)