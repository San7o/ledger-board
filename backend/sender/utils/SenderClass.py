"""The sender class."""
from kafka import KafkaProducer
import logging
logger = logging.getLogger('django')

class SenderClass:

    """The sender class.
    This class is used to send data to the server, interacting with kafka as the message broker.
    Contains three methods:
    - send: Sends a message to the server without a key.
    - send_key: Sends a message to the server with a key.
    - __init__: Initializes the KafkaProducer object.
    """

    def __init__(self):
        """Initializes the KafkaProducer object."""
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def send(self, topic, message) -> bool:
        """Sends a message to the server without a key."""
        try:
            self.producer.send(topic, message.encode())
            self.producer.flush()

            logger.info( { "topic": topic, "message": message } )
        
            return True

        except Exception as e:

            logger.error(e)
            
            return False

    def send_key(self, topic, key, message) -> bool:
        """Sends a message to the server with a key."""
        try:
            self.producer.send(topic, key=key.encode(), value=message.encode())
            self.producer.flush()

            logger.info({ "topic": topic, "key": key, "message": message })
        
            return True

        except Exception as e:
            
            logger.error(e)
            
            return False
