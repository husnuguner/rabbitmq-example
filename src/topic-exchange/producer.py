import sys

from prepare import CONFIG
from src.util import connection

DATA = [
    {"brand": "ferrari", "type": "car", "color": "red", "year": 2015, "trouble": "Yes"},
    {"brand": "ferrari", "type": "car", "color": "blue", "year": 2020, "trouble": "No"},

    {"brand": "bmw", "type": "car", "color": "yellow", "year": 2019, "trouble": "Yes"},
    {"brand": "bmw", "type": "car", "color": "black", "year": 2020, "trouble": "No"},

    {"brand": "bmw", "type": "bike", "color": "purple", "year": 2018, "trouble": "Yes"},
    {"brand": "bmw", "type": "bike", "color": "green", "year": 2019, "trouble": "No"},

    {"brand": "salcano", "type": "bike", "color": "white", "year": 2017, "trouble": "Yes"}
]


def main(i):
    message = DATA[i] if i < len(DATA) else DATA[0]

    routing_key = '%s.%s.%s' % (message["brand"], message['type'], message['color'])

    conn, channel = connection.create()

    channel.basic_publish(exchange=CONFIG["exchange"],
                          routing_key=routing_key,
                          body=str(message))

    print(" [x] Sent %r" % message)

    conn.close()


if __name__ == '__main__':
    # get integer from sys.argv
    index = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    main(index)
