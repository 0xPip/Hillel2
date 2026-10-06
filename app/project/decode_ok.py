import jwt
import datetime

secret = "my_super_secret_key_for_jwt_12345"

payload = {
    "surname": "Polishchuk",
    "group": "25.08.26",
    "subject": "Python",
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30),
}

token = jwt.encode(payload, secret, algorithm="HS256")
print("Токен:", token)

decoded = jwt.decode(token, secret, algorithms=["HS256"])
print("Декодовано успішно:", decoded)