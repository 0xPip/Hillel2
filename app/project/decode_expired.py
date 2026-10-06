import jwt
import datetime

secret = "my_secret_key"

payload = {
    "surname": "Polishchuk",
    "group": "ПС-25.08.2026",
    "subject": "Python",
    "exp": datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=1),
}

token = jwt.encode(payload, secret, algorithm="HS256")
print("Токен:", token)

decoded = jwt.decode(token, secret, algorithms=["HS256"])
print(decoded)
