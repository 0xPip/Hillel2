import os
from dotenv import load_dotenv

load_dotenv()

AMQP_HOST = os.getenv('AMQP_HOST')
AMQP_PORT = os.getenv('AMQP_PORT')
AMQP_VIRTUAL_HOST = os.getenv('AMQP_VIRTUAL_HOST')
AMQP_USERNAME = os.getenv('AMQP_USERNAME')
AMQP_PASSWORD = os.getenv('AMQP_PASSWORD')