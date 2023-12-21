import sys

import pika

from prepare import CONFIG
from src.util import connection


def main(message):
    conn, channel = connection.create()

    channel.basic_publish(exchange=CONFIG["exchange"],
                          routing_key="",  # The routing key is ignored for headers exchanges.
                          properties=pika.BasicProperties(
                              headers={"status": "SUCCESS"}
                          ),
                          body=message)

    print(" [x] Sent %r" % message)

    conn.close()


if __name__ == '__main__':
    example = ' '.join(sys.argv[1:]) or "Hello World! Example"

    main(example)
