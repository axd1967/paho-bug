from __future__ import absolute_import

from paho.mqtt.client import error_string

from MQTTClient import MyClient

from consts import TOPIC2


def main():

    client = MyClient()
    run(client)


def run(client):

    while True:

        # FIXME when continuing ('c'), here things go wrong
        import pdb; pdb.set_trace()

        result, mid = client.publish(TOPIC2, "this is going to crash", qos=2)
        print("mid={} res={}".format(mid, error_string(result)))

if __name__ == "__main__":
    main()
