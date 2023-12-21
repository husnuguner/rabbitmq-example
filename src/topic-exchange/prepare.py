from pika.exchange_type import ExchangeType

from src.util import connection

CONFIG = {
    "exchange": "topic.exchange",
    "queues": [
        {"name": "ferrari.queue", "routing": ["ferrari.car.*"]},

        {"name": "bmw.car.queue", "routing": ["bmw.car.*"]},
        {"name": "bmw.bike.queue", "routing": ["bmw.bike.*"]},

        {"name": "salcano.bike.queue", "routing": ["salcano.bike.*"]},

        {"name": "all.bike.queue", "routing": ["*.bike.*", "#.bike.#"]},
        {"name": "all.car.queue", "routing": ["*.car.*", "#.car.#"]},

    ]
}


def prepare():
    conn, channel = connection.create()
    # Create an exchange
    print(" [x] Creating exchange '{}'".format(CONFIG["exchange"]))
    channel.exchange_declare(exchange=CONFIG["exchange"],
                             exchange_type=ExchangeType.topic,  # ExchangeType değerini vermek zorundayız,
                             durable=True)

    for queue in CONFIG["queues"]:
        # Create a queue
        print(" [x] Creating queue '{}'".format(queue["name"]))
        channel.queue_declare(queue=queue["name"],
                              durable=True)

        # Bind queue to exchange
        for routing_key in queue["routing"]:
            print(" [x] Binding queue '{}' to exchange '{}' with routing key '{}'".format(
                queue["name"], CONFIG["exchange"], routing_key))
            channel.queue_bind(exchange=CONFIG["exchange"],
                               queue=queue["name"],
                               routing_key=routing_key)


if __name__ == '__main__':
    prepare()
