import os

import redis
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("REDIS_HOST")
port = int(os.getenv("REDIS_PORT"))
password = os.getenv("REDIS_PASSWORD")

r = redis.Redis(host=host, port=port, password=password, decode_responses=True)

pubsub = r.pubsub(ignore_subscribe_messages=True)
pubsub.subscribe("python_channel")

print("Слухаю канал python_channel...")

for message in pubsub.listen():
    print(message["data"])
