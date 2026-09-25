from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')

password = 'aa'
print(11111111)
hash = context.hash(secret=password)

print(hash)
print(22222222)


user_pass = 'aa'

is_valid = context.verify(user_pass, hash)
print(is_valid)