# -*- coding: utf-8 -*-
from threading import Thread
import json
import socket
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



class piHandler(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """

        # Flag to run thread as a deamon
        super(piHandler, self).__init__()
        self.daemon = True
        self.connection = connection
        self.client = client
        print "piHandler started"

        # TODO: Finish initialization of MessageReceiver

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            response = self.connection.recv(1024)
            # print Message
            # print response
            Message = json.loads(str(response))
            print Message
            print type(Message)
            #a = ast.literal_eval(Message)
            #print "Message[signal]="+Message['signal']+"\n"
            colour = Message['signal']
            if colour=='red':
                sense.show_message(message1, speed, text_colour=red, back_colour= red)
                
