from src.util import connection

CONFIG = {
    "queue": "default.queue",
}


def prepare():
    conn, channel = connection.create()
    # Create a queue
    print(" [x] Creating queue '{}'".format(CONFIG["queue"]))
    channel.queue_declare(queue=CONFIG["queue"],
                          durable=True)


if __name__ == '__main__':
    prepare()
