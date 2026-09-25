import os
from dotenv import load_dotenv
import redis

load_dotenv()

host = os.getenv("REDIS_HOST")
port = int(os.getenv("REDIS_PORT"))
password = os.getenv("REDIS_PASSWORD")

r = redis.Redis(host=host, port=port, password=password, decode_responses=True)

# улюблена модель авто
r.set("favorite_car", "Mercedes e63s")

# улюблений домашній улюбленець - зникне через 2 години
r.set("favorite_pet", "Dog")
r.expire("favorite_pet", 7200)

# список продуктів для закупівлі
r.rpush("shopping_list", "молоко", "хліб", "яйця", "цукор")
r.expire("shopping_list", 604800)

# словник - інгредієнти торта
r.hset("cake_ingredients", mapping={"flour": 250, "milk": 500})

# додати цукор 300 грам
r.hset("cake_ingredients", "sugar", 300)

# виправити цукор на 500 грам
r.hset("cake_ingredients", "sugar", 500)