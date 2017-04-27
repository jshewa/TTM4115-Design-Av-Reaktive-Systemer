__author__ = 'Jakob'
import socket
import json

class App:

    def __init__(self,port):
        self.client = socket.socket()
        self.port = port
        self.client.connect(("10.22.66.215", port))

    def run(self):
        print("Starting connection")
        while True:
            try:
                print(self.client.recv(4096).decode('utf-8'))
            except Exception as e:
                print(e)
                return

if __name__ == '__main__':
    app = App(13001)
    app.run()