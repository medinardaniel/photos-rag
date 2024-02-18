from generate_signed_url import generate_signed_url
from config import Config  # Ensure this import path matches where your Config class is defined

def main():
    # Replace 'example-image.jpg' with the actual file name in your S3 bucket
    object_name = 'IMG_0127.jpeg'
    print("Bucket:", Config.S3_BUCKET)
    
    # Call your function to generate a signed URL
    signed_url = generate_signed_url(Config.S3_BUCKET, object_name)
    
    if signed_url:
        print("Signed URL:", signed_url)
    else:
        print("Failed to generate signed URL.")

if __name__ == "__main__":
    main()
