# -*- coding: utf-8 -*-
from threading import Thread
import json
import time
import RPi.GPIO as GPIO




class gpsrecieve(Thread):
 
    RED = 18
    YELLOW = 19
    GREEN = 20
  

    def __init__(self, client, connection):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(RED,GPIO.OUT) #Red
        GPIO.setup(YELLOW,GPIO.OUT) #Yellow
        GPIO.setup(GREEN,GPIO.OUT) #Green
        self.init_led()




        # Flag to run thread as a deamon
        super(GPS, self).__init__()
        self.daemon = True
        self.connection = connection
        self.client = client
        


        # TODO: Finish initialization of MessageReceiver

    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while True:
            response = self.connection.recv(1024)
            # print Message
            # print response
            Message = json.loads(str(response))
            print "Message[signal]=",Message['signal'],"\n"
            switch_led(Message['signal'])

    
    def switch_led(colour):


        if colour == "red":
            print "come back signal"
            GPIO.output(RED,GPIO.HIGH)
            self.pin_high =RED

        elif colour == "Yellow"
            print   "do something"
            GPIO.output(YELLOW,GPIO.HIGH)
            self.pin_high = YELLOW
        elif colour == "Green"
            print "All good"
            GPIO.output(GREEN,GPIO.HIGH)
            self.pin_high = GREEN


    def init_led():
        GPIO.output(RED,GPIO.LOW)
        GPIO.output(YELLOW,GPIO.LOW)
        GPIO.output(GREEN, GPIO.HIGH)
        self.pin_high = GREEN

