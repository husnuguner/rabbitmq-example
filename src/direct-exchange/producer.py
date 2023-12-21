import sys

from prepare import CONFIG
from src.util import connection


def main(message):
    conn, channel = connection.create()

    channel.basic_publish(exchange=CONFIG["exchange"],
                          routing_key=CONFIG["routing_key"],
                          body=message)

    print(" [x] Sent %r" % message)

    conn.close()


if __name__ == '__main__':
    example = ' '.join(sys.argv[1:]) or "Hello World! Example"

    main(example)
