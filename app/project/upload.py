import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION_NAME"),
)

filename = "Artem_Polishchuk.html"

s3.upload_file(
    filename,
    os.getenv("AWS_BUCKET_NAME"),
    filename,
    ExtraArgs={
        "ContentType": "text/html"
    }
)

public_url = f"{os.getenv('AWS_PUBLIC_URL')}/{filename}"

print("Файл успішно завантажено!")
print("Посилання:")
print(public_url)