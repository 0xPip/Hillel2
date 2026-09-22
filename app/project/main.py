from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "MySecret123"
wrong_password = "WrongPassword"

hashed = pwd_context.hash(password)

print("Password:", password)
print("Hash:", hashed)
print("Correct password valid:", pwd_context.verify(password, hashed))
print("Wrong password valid:", pwd_context.verify(wrong_password, hashed))