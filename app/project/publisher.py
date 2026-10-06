import os

import redis
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("REDIS_HOST")
port = int(os.getenv("REDIS_PORT"))
password = os.getenv("REDIS_PASSWORD")

r = redis.Redis(host=host, port=port, password=password, decode_responses=True)

r.publish("python_channel", "Hello Redis! Message #0")
r.publish("python_channel", "Hello Redis! Message #1")
r.publish("python_channel", "Hello Redis! Message #2")
r.publish("python_channel", "Hello Redis! Message #3")
r.publish("python_channel", "Hello Redis! Message #4")
r.publish("python_channel", "Hello Redis! Message #5")
r.publish("python_channel", "Hello Redis! Message #6")
r.publish("python_channel", "Hello Redis! Message #7")
r.publish("python_channel", "Hello Redis! Message #8")
r.publish("python_channel", "Hello Redis! Message #9")

print("Надіслано 10 повідомлень у python_channel")
