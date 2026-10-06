from pika.adapters import blocking_connection
from amqp_utils.amqp_client import get_connection
import time


def process_new_message(channel, method, properties, body: bytes):
    print(body)
    time.sleep(2)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def consume_message(channel: blocking_connection.BlockingChannel):
    QUEUE = 'weather'

    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
    )
    channel.start_consuming()


def main_consumer():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_message(channel)