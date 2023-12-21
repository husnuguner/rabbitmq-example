from pika.exchange_type import ExchangeType

from src.util import connection

CONFIG = {
    "exchange": "headers.exchange",
    "queue": "headers.queue"
}


def prepare():
    conn, channel = connection.create()
    # Create an exchange
    print(" [x] Creating exchange '{}'".format(CONFIG["exchange"]))
    channel.exchange_declare(exchange=CONFIG["exchange"],
                             exchange_type=ExchangeType.headers,  # ExchangeType değerini vermek zorundayız,
                             durable=True)

    # Create a queue
    print(" [x] Creating queue '{}'".format(CONFIG["queue"]))
    channel.queue_declare(queue=CONFIG["queue"],
                          durable=True)

    # Bind queue to exchange
    print(" [x] Binding queue '{}' to exchange '{}'".format(CONFIG["queue"], CONFIG["exchange"]))
    channel.queue_bind(exchange=CONFIG["exchange"],
                       queue=CONFIG["queue"],
                       arguments={
                           "x-match": "any",  # We can use "all" or "any"
                           "status": "SUCCESS"
                       })


if __name__ == '__main__':
    prepare()
