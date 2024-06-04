"""The sender class."""

from .celeryApp import app
from kafka import KafkaProducer
import logging

logger = logging.getLogger('django')

producer = None


class SenderClass:

    """The sender class.
    This class is used to send data to the server,
    interacting with kafka as the message broker.
    Contains two methods:
    - send: Sends a message to the server without a key.
    - send_key: Sends a message to the server with a key.

    To call the methods, use the following syntax:
    - SenderClass.send.delay(topic, message)
    - SenderClass.send_key.delay(topic, key, message)
    """

    @app.task
    def send(topic, message):
        """Sends a message to the server without a key."""
        try:

            print("Sending message", message)
            producer = KafkaProducer(bootstrap_servers='localhost:9092')

            producer.send(topic, message.encode())

            # for testing purposes
            producer.flush()

            logger.info({"topic": topic, "message": message})
            print("Message sent")

            # Closing to avoid memory leaks
            producer.close()

        except Exception as e:

            logger.error(e)
            print("Error sending message")

    @app.task
    def send_key(topic, key, message):
        """Sends a message to the server with a key."""
        try:

            print("Sending message", message)
            producer = KafkaProducer(bootstrap_servers='localhost:9092')

            producer.send(topic, key=key.encode(), value=message.encode())

            # for testing purposes
            producer.flush()

            logger.info({"topic": topic, "key": key, "message": message})
            print("Message sent")

            # Closing to avoid memory leaks
            producer.close()

        except Exception as e:

            logger.error(e)
            print("Error sending message")
