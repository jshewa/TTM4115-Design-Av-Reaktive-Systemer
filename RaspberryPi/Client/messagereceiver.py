# -*- coding: utf-8 -*-
from threading import Thread
import json
import time
import RPi.GPIO as GPIO




class GPS(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT) #Red
        GPIO.setup(19,GPIO.OUT) #Green
        GPIO.setup(20,GPIO.OUT) #Yellow




        # Flag to run thread as a deamon
        super(GPS, self).__init__()
        self.daemon = True
        self.connection = connection
        self.client = client
        self.pin_high= 20


        # TODO: Finish initialization of MessageReceiver

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            response = self.connection.recv(1024)
            # print Message
            # print response
            Message = json.loads(str(response))
            print "Message[signal]=%s", %(Message['signal'])
            turn_led_On(Message['signal'])

    
    def turn_led_On(colour)



        if colour == "red":
            print "come back signal"
            GPIO.output(18,GPIO.HIGH)
            self.pin_high = 18

        elif colour == "Yellow"
            print   "do something"
            GPIO.output(20,GPIO.HIGH)
            self.pin_high = 20
        elif colour == "Green"
            print "All good"
            GPIO.output(19,GPIO.HIGH)
            self.pin_high = 19





        return 1

    def turn_led_Off(colour)


        return 1
