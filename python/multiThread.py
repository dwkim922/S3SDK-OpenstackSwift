import boto3
import os
import sys
import time
from multiprocessing.pool import ThreadPool

# Thread 정해주면됨
threads=20 

# Configure AWS credentials and region
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = ''
endpoint_url=''

# Initialize the S3 client
s3_client = boto3.client('s3', region_name=aws_region,
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         endpoint_url=endpoint_url)

def upload_part(bucket_name, key, part_number, part_data, upload_id):
    try:
        response = s3_client.upload_part(
            Bucket=bucket_name,
            Key=key,
            PartNumber=part_number,
            UploadId=upload_id,  # Include the UploadId
            Body=part_data
        )
        return {'PartNumber': part_number, 'ETag': response['ETag']}
    except Exception as e:
        return {'PartNumber': part_number, 'Error': str(e)}

def multipart_upload(bucket_name, key, file_path, part_size=5 * 1024 * 1024):
    # Calculate the total number of parts and file size
    file_size = os.path.getsize(file_path)
    total_parts = (file_size + part_size - 1) // part_size
    
    # Create a multipart upload
    response = s3_client.create_multipart_upload(Bucket=bucket_name, Key=key)
    upload_id = response['UploadId']

    # Create a ThreadPool to upload parts in parallel
    pool = ThreadPool(processes=threads)  

    # Upload parts in parallel
    with open(file_path, 'rb') as file:
        parts = []
        for part_number in range(1, total_parts + 1):
            part_data = file.read(part_size)
            if part_data:
                parts.append((bucket_name, key, part_number, part_data, upload_id))
        
        results = pool.starmap(upload_part, parts)

    # Verify if all parts were successfully uploaded
    for result in results:
        if 'Error' in result:
            s3_client.abort_multipart_upload(
                Bucket=bucket_name,
                Key=key,
                UploadId=upload_id
            )
            print(f"Failed to upload part {result['PartNumber']}: {result['Error']}")
            sys.exit(1)

    # Complete the multipart upload
    parts_info = [{'PartNumber': result['PartNumber'], 'ETag': result['ETag']} for result in results]
    s3_client.complete_multipart_upload(
        Bucket=bucket_name,
        Key=key,
        UploadId=upload_id,
        MultipartUpload={'Parts': parts_info}
    )
    print(f"Successfully uploaded {key}")

if __name__ == "__main__":
    bucket_name = 'new-bucket-1c6c055d'
    key = 'upload_test'
    file_path = 'AWSTraining.rar'

    start_time = time.time()
    multipart_upload(bucket_name, key, file_path)
    end_time = time.time()

    duration = end_time - start_time
    file_size = os.path.getsize(file_path)
    upload_speed = file_size / (1024 * 1024 * duration)  # MB/s

    print(f"Upload duration: {duration:.2f} seconds")
    print(f"Upload speed: {upload_speed:.2f} MB/s")
