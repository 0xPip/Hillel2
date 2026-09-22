import jwt
import datetime

secret = "my_secret_key"

payload = {
    "surname": "Ivanenko",
    "group": "KN-21",
    "subject": "Python",
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30),
}

token = jwt.encode(payload, secret, algorithm="HS256")

print("Token:")
print(token)