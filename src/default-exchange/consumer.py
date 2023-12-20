import sys

from prepare import CONFIG
from src.util import connection


def main():
    conn, channel = connection.create()

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

        # ch.basic_reject(delivery_tag=method.delivery_tag)
        # ch.basic_nack(delivery_tag=method.delivery_tag)
        ch.basic_ack(delivery_tag=method.delivery_tag)  # if auto_ack=False

    channel.basic_consume(queue=CONFIG["queue"],
                          on_message_callback=callback,
                          auto_ack=False)

    print(" [*] Waiting for messages from queue %r. To exit press CTRL+C" % CONFIG["queue"])
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' [*] Interrupted')
        sys.exit(0)
