from __future__ import absolute_import
from paho.mqtt import client as mqttclient

from consts import BROKER
from paho.mqtt.client import error_string

CLIENT_ID = "my_client_id"


class MyClient(mqttclient.Client):
    def __init__(self):
        super(MyClient, self).__init__(CLIENT_ID)

        self.username_pw_set("client_app", "client_pass")
        self.connect(BROKER)

        self.loop_start()

    def on_log(self, client, userdata, level, buf):
        print("on_log: ud:{} level:{} buf:{}".format(userdata, level, buf))

    def on_connect(self, client, userdata, flags, rc):
        if not rc:
            print("connected OK")
        else:
            print("*** WARNING!: conn issue: data={}, flags={}, rc={}s".format(userdata, flags, rc))

    def on_disconnect(self, client, userdata, result):
        print("on_disconn: data={}, r={}".format(userdata, error_string(result)))

    def on_publish(self, client, userdata, mid):
        print("on_publish: data={}, mid={}".format(userdata, mid))

