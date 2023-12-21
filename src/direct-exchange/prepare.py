from pika.exchange_type import ExchangeType

from src.util import connection

CONFIG = {
    "exchange": "direct.exchange",
    "queue": "direct.queue",
    "routing_key": "direct.key",
}


def prepare():
    conn, channel = connection.create()
    # Create an exchange
    print(" [x] Creating exchange '{}'".format(CONFIG["exchange"]))
    channel.exchange_declare(exchange=CONFIG["exchange"],
                             exchange_type=ExchangeType.direct,  # ExchangeType değerini vermek zorundayız,
                             durable=True)

    # Create a queue
    print(" [x] Creating queue '{}'".format(CONFIG["queue"]))
    channel.queue_declare(queue=CONFIG["queue"],
                          durable=True)

    # Bind queue to exchange
    print(" [x] Binding queue '{}' to exchange '{}' with routing key '{}'".format(
        CONFIG["queue"], CONFIG["exchange"], CONFIG["routing_key"]))
    channel.queue_bind(exchange=CONFIG["exchange"],
                       queue=CONFIG["queue"],
                       routing_key=CONFIG["routing_key"])


if __name__ == '__main__':
    prepare()
