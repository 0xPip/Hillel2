import jwt
import datetime

secret = "my_secret_key"

payload = {
    "surname": "Polishchuk",
    "group": "ПС-25.08.2026",
    "subject": "Python",
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30),
}

token = jwt.encode(payload, secret, algorithm="HS256")

print(token)
