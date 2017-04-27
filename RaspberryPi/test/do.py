# -*- coding: utf-8 -*-
import socket
import json
import time
import datetime
import math
import RPi.GPIO as GPIO
import struct
import sys
import random
import ast
from sense_hat import SenseHat



yellow = (255, 255, 51)
blue = (0, 102, 255)
white= (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
message1 = ""
message2 = ""


speed = 0.05
i=0
sense = SenseHat()


def get_random_port():
    return random.randint(10000, 11000)


class Client:

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """
       
        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = get_random_port()
        # self.connection.bind(('localhost', port))
        # TODO: Finish init process with necessary code /done

        self.server_port = server_port
        self.host = host


        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        print "connection up"
        curr_time = datetime.datetime.fromtimestamp(
            time.time()).strftime('%H:%M:%S')
        print "<%s> [%s]: ----*Connection established*---- " 
        self.do()

    def disconnect(self):
        print "Closing Socket\n"
        self.connection.close()


    def do(self):
   
       while True:
            response = self.connection.recv(1024)
            # print Message
            # print response
            Message = json.loads(response.decode('utf-8'))
            print Message
            print type(Message)
            a = ast.literal_eval(Message)
            #print "Message[signal]="+Message['signal']+"\n"
            colour = a['signal']
            if colour=='red':
                sense.show_message(message1, speed, text_colour=red, back_colour= red)
                


   

 


if __name__ == '__main__':
  
    client = Client('10.22.66.215', 13000)
