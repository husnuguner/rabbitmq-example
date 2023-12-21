from pika.exchange_type import ExchangeType

from src.util import connection

CONFIG = {
    "exchange": "fanout.exchange",  # Use for Pub/Sub pattern
    "queue": "fanout.queue",
}


def prepare():
    conn, channel = connection.create()
    # Create an exchange
    print(" [x] Creating exchange '{}'".format(CONFIG["exchange"]))
    channel.exchange_declare(exchange=CONFIG["exchange"],
                             exchange_type=ExchangeType.fanout,  # ExchangeType değerini vermek zorundayız,
                             durable=True)

    # Create a queue
    for i in range(1, 4):
        queue_name = CONFIG["queue"] + "." + str(i)

        print(" [x] Creating queue '{}'".format(queue_name))
        channel.queue_declare(queue=queue_name,
                              durable=True)

        print(" [x] Binding queue '{}' to exchange '{}'".format(queue_name, CONFIG["exchange"]))
        channel.queue_bind(exchange=CONFIG["exchange"],
                           queue=queue_name)


if __name__ == '__main__':
    prepare()
