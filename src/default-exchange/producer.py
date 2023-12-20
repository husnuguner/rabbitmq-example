import sys

from prepare import CONFIG
from src.util import connection


def main(message):
    conn, channel = connection.create()

    # We don't exchange declare because we use default exchange
    # We use queue name as routing key because we use default exchange
    # We can use 'default' and empty string as exchange name for using default exchange
    channel.basic_publish(exchange='',
                          routing_key=CONFIG["queue"],
                          body=message)

    print(" [x] Sent %r" % message)

    conn.close()


if __name__ == '__main__':
    example = ' '.join(sys.argv[1:]) or "Hello World! Example"

    main(example)
