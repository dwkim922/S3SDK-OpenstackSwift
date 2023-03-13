import boto3

session = boto3.session.Session(profile_name='zadara')

s3_client = session.client(
    service_name='s3',
    region_name='us-east-1',
    endpoint_url='',
)

# Uncomment if you want to set multipart
#config = TransferConfig(multipart_threshold=1024 * 25, #if 25MB or above, will initiate multipart
#                        max_concurrency=20,
#                        multipart_chunksize=1024 * 10, #segment will be 10MB
#                        use_threads=True)

objectName = 'test.txt'
bucket = 'tempurl'

response = s3_client.upload_file(
    objectName, bucket, objectName,
    ExtraArgs={'ContentType': 'abc/test'}
#    Config=config #Uncomment for multipart config 
     )
