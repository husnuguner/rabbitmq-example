import pika


def create():
    credentials = pika.PlainCredentials("guest", "guest")
    parameters = pika.ConnectionParameters(host="localhost", credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return connection, channel
