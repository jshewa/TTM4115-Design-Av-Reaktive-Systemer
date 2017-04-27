# -*- coding: utf-8 -*-
import socket
import json
import thread
import time
import datetime
from piHandler import piHandler
import random






class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # self.connection.bind(('localhost', port))
        # TODO: Finish init process with necessary code /done

        self.server_port = server_port
        self.host = host
        self.payload = {'ID': 1,'LAT': 2,'LONG' : 3,'NAME':"pi"}
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        #self.get_data()
        self.send_payload()
        curr_time = datetime.datetime.fromtimestamp(
            time.time()).strftime('%H:%M:%S')
        print "<%s> [%s]: ----*Connection established*---- " 
        self.receive_message()
        while 1:
            #self.get_data()
            self.send_payload()
            time.sleep(5)

    def disconnect(self):
        print "Closing Socket\n"
        thread.exit()
        self.connection.close()

        # TODO: Handle disconnection/done

    def receive_message(self):
        # TODO: Handle incoming message
        rsp = piHandler(self, self.connection)
        rsp.start()

    def send_payload(self):
        # TODO: Handle sending of a payload

        self.connection.sendall(json.dumps(self.payload))
        # print "Sending request\n"

    """def get_data(self):

        # print "Possible requests: \n login\n logout \n msg \n names \n help\n
        # disconnect\n"

        while 1:
            time.sleep(0.3)
            curr_time = datetime.datetime.fromtimestamp(
                time.time()).strftime('%H:%M:%S')
            self.payload['request'] = raw_input(
                "<%s> [request]: " % (curr_time))
            if self.payload['request'] == "login":
                self.payload['content'] = raw_input(
                    "<%s> [enter username]:" % (curr_time))
                self.name = self.payload['content']
                break
            elif self.payload['request'] == "logout":
                self.payload['content'] = None
                self.send_payload()
                self.disconnect()
                break
            elif self.payload['request'] == "msg":
                self.payload['content'] = raw_input(
                    "<%s> [enter msg]: " % (curr_time))
                break
            elif self.payload['request'] == "names":
                self.payload['content'] = None
                break
            elif self.payload['request'] == "help":
                self.payload['content'] = None
                break
            else:
                print "<%s> [%s]: Invalid request!" % (curr_time, self.name)

        print "<%s> [%s]: Request accepted" % (curr_time, self.name)"""

    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('10.22.76.166', 13000)
