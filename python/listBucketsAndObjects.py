import boto3

session = boto3.session.Session(profile_name='zadara')

s3_client = session.client(
    service_name='s3',
    region_name='us-east-1',
    endpoint_url='',
)

print('Buckets')
print(s3_client.list_buckets())

print('')

print('Objects')
print(s3_client.list_objects(Bucket='tempurl'))
