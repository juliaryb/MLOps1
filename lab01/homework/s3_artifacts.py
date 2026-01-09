import boto3
import os

# create an S3 resource object
s3 = boto3.resource(
    "s3"
)  # assumes credentials & configuration are handled outside python in .aws directory or environment variables

BUCKET_NAME = "mlops-9-bucket"
S3_MODELS_PREFIX = "model/"
LOCAL_MODELS_DIR = "model"


def download_models_from_s3():
    # don't download if models are present
    if os.path.exists(LOCAL_MODELS_DIR) and os.listdir(LOCAL_MODELS_DIR):
        return

    bucket = s3.Bucket(BUCKET_NAME)  # get a handle to the S3 bucket

    for obj in bucket.objects.filter(Prefix=S3_MODELS_PREFIX):
        # keep the same structure locally
        local_path = obj.key
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        bucket.download_file(obj.key, local_path)
