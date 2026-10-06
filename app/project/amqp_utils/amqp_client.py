import pika
import ssl

import config

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(
    host=config.AMQP_HOST,
    port=int(config.AMQP_PORT),
    virtual_host=config.AMQP_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=config.AMQP_USERNAME, password=config.AMQP_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)