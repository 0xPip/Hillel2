from pika.adapters import blocking_connection
from amqp_utils.amqp_client import get_connection
import time


def produce_message(channel: blocking_connection.BlockingChannel) -> None:
    QUEUE = 'weather'
    channel.queue_declare(QUEUE)

    message = 'Weather from Artem Polishchuk: sunny, {item} degrees'
    for item in range(600):
        time.sleep(0.1)
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=message.format(item=item)
        )
        print(item)


def main_producer():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_message(channel)