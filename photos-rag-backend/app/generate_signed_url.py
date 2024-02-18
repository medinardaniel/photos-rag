import boto3
from botocore.exceptions import NoCredentialsError
from .config import Config

def generate_signed_url(bucket_name, object_name, expiration=3600):
    """
    Generate a signed URL to access an S3 object

    :param bucket_name: String name of the bucket
    :param object_name: String name of the object
    :param expiration: Time in seconds for the signed URL to remain valid
    :return: Signed URL as a string. If error, returns None.
    """
    # Create a boto3 S3 client
    s3_client = boto3.client('s3')

    try:
        # Generate the signed URL for GET request
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        print("Credentials not available")
        return None

    return response

def get_signed_urls(filenames):
    """
    Generate a signed URL for each object in the object_names list

    :param bucket_name: String name of the bucket
    :param object_names: List of object names
    :return: List of signed URLs
    """
    bucket_name = Config.S3_BUCKET
    signed_urls = {}
    for object_name in filenames:
        signed_url = generate_signed_url(bucket_name, object_name)
        if signed_url:
            signed_urls[object_name] = signed_url
    return signed_urls