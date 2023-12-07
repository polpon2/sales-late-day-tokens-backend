import pika, sys, json
from opentelemetry.instrumentation.pika import PikaInstrumentor

PikaInstrumentor().instrument()

class RabbitMQConnection:
    _instance = None

    def __new__(cls, host="localhost", port=5672):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host="localhost", port=5672):
        self.host = host
        self.port = port
        self.connection = None
        self.channel = None
        self.connect()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
            self.channel = self.connection.channel()
            print("Connected to Rabbit Mq")
        except:
            sys.exit("Could not connect to RabbitMq")

    def create_channel(self):
        self.channel = self.connection.channel();

    def is_connected(self):
        return self.connection is not None and self.connection.is_open

    def close(self):
        if self.is_connected():
            self.connection.close()
            self.connection = None
            print("RabbitMQ connection closed")

    def _publish_to_queue(self, queue_name, data):

        self.channel.basic_publish(exchange="",
                                    routing_key=queue_name,
                                    body=data)
        print(f" [x] Sent to '{queue_name}'")

    def send_data(self, queue_name, data):
        """Publish msg, reconnecting if necessary."""

        try:
            self._publish_to_queue(queue_name, data)
            return True
        except:
            print('reconnecting to queue...')
            self.connect()
            self._publish_to_queue(queue_name, data)
            return True