import sys

from prepare import CONFIG
from src.util import connection


def main(queue_name):
    conn, channel = connection.create()

    def callback(ch, method, properties, body):
        print(" [x] Received from %r: %r" % (queue_name, body.decode()))

        # ch.basic_reject(delivery_tag=method.delivery_tag)
        # ch.basic_nack(delivery_tag=method.delivery_tag)
        ch.basic_ack(delivery_tag=method.delivery_tag)  # if auto_ack=False

    channel.basic_consume(queue=queue_name,
                          on_message_callback=callback,
                          auto_ack=False)

    print(" [*] Waiting for messages from queue %r. To exit press CTRL+C" % queue_name)
    channel.start_consuming()


if __name__ == '__main__':
    qn = ' '.join(sys.argv[1:]) or CONFIG["queue"]
    try:
        main(qn)
    except KeyboardInterrupt:
        print(' [*] Interrupted')
        sys.exit(0)

# Usage: py consumer.py fanout.queue.1
# Usage: py consumer.py fanout.queue.2
# Usage: py consumer.py fanout.queue.3
