# aws-services
a small project idea that involves using AWS services. It focuses on building a serverless web application to upload, store, and view images.

Services Used
Amazon S3: To store the uploaded images.
AWS Lambda: To process and validate the images upon upload.
API Gateway: To create an API endpoint for uploading images.
Amazon DynamoDB (optional): To store metadata about the uploaded images (e.g., image name, upload timestamp).
AWS CloudFront: To distribute and cache the images globally (optional for performance).

Steps to Build
1. Setup an S3 Bucket
Create an S3 bucket (e.g., my-image-storage-bucket).
Enable public access or use pre-signed URLs for controlled access.
2. Build a Lambda Function
Write a Lambda function in Python to validate and process the uploaded images.
