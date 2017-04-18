__author__ = 'Jakob'
__author__ = 'Jakob'
import socket
import json
import random


class Client:

    def __init__(self):
        self.client = socket.socket()
        self.payload = {'id': 1, 'time': 2556,'lat' : 9283, 'long' : 760}
        port = 13000
        self.client.connect((socket.gethostname(), port))

    def run(self):
        print("Starting connection")
        while True:
            try:
                self.send_payload()
            except Exception as e:
                print(e)
                return


    def send_payload(self):
        self.randomVals(self.payload)
        self.client.sendall(json.dumps(str(self.payload)).encode('utf-8'))

    def randomVals(self,payload):
        random_tall1 = random.randint(0,10000)
        random_tall2 = random.randint(0,10000)
        random_tall3 = random.randint(0,10000)
        self.payload['time'] = random_tall1
        self.payload['lat'] = random_tall2
        self.payload['long'] = random_tall3
        self.payload['id'] = 1


if __name__ == '__main__':
    client = Client()
    client.run()