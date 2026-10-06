import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

pubsub = r.pubsub(ignore_subscribe_messages=True)
pubsub.subscribe("python_channel")

print("Слухаю канал python_channel...")

for message in pubsub.listen():
    print(message["data"])