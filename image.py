import boto3
import os
import uuid

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ['BUCKET_NAME']
    file_content = event['body']
    file_name = str(uuid.uuid4()) + ".jpg"

    # Upload to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content,
        ContentType='image/jpeg'
    )

    return {
        "statusCode": 200,
        "body": f"Image {file_name} uploaded successfully!"
    }
