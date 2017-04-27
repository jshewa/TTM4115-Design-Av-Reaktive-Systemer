# -*- coding: utf-8 -*-
import socket
import json
import thread
import time
import datetime
import serial, time
import smbus
import math
import RPi.GPIO as GPIO
import struct
import sys
import random
from gps_do import gpsrecieve

ser = serial.Serial('/dev/serial0',  9600, timeout = 0)	#Open the serial port at 9600 baud
ser.flush()

def readlineCR():
    rv = ""
    while True:
        time.sleep(0.001)	# This is the critical part.  A small pause 
        					# works really well here.
        ch = ser.read()        
        rv += ch
        if ch=='\r' or ch=='':
            return rv
 



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
        self.payload = {'id': None, 'time': None,'lat' : None, 'long' : None}
        self.id = "1"
        self.time = None
        self.fix  = None
        self.sats = None
        self.alt  = None
        self.lat  = None
        self.lat_ns = None
        self.long = None
        self.long_ew= None
        self.inp=[]
        self.GGA=[]





        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        print "connection up"
        curr_time = datetime.datetime.fromtimestamp(
            time.time()).strftime('%H:%M:%S')
        print "<%s> [%s]: ----*Connection established*---- " % (curr_time, self.id)
        self.receive_message()
        self.do()

    def disconnect(self):
        print "Closing Socket\n"
        thread.exit()
        self.connection.close()

        # TODO: Handle disconnection/done

    def receive_message(self):
        # TODO: Handle incoming message
        # TODO: TURN LED ON
        rsp = gpsrecieve(self, self.connection)
        rsp.start()

    def send_payload(self):
        # TODO: Handle sending of a payload

        self.connection.sendall(json.dumps(self.payload))

    def do(self):
        
        """f=open("self_data.csv",'w')	#Open file to log the data
        print " Writing file"
        f.write("name,latitude,longitude\n")	#Write the header to the top of the file
        print " write file done"
        ind=0"""
        
        while True:
            try:
                print "READING FILE"
                #self.read()	#Read from self
                #self.vals()	#Get the individial values
                #print "Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",long,long_ew
                #s=str(t)+","+str(float(self.lat)/100)+","+str(float(self.long)/100)+"\n"	
                #f.write(s)	#Save to file
                #self.payload['time'] = self.time
                #self.payload['long'] = self.lat
                #self.payload['lat' ] = self.long
                
                self.payload['time'] = 2
                self.payload['long'] = 24
                self.payload['lat' ] = 50
                
                print "sending"
                self.send_payload()
                time.sleep(2)
                

            except IndexError:
                print "Unable to read"
            #except KeyboardInterrupt:
                #f.close()
                #print "Exiting"
                #sys.exit(0)
            #except:
                #print "Raw String appears to be empty."
                # self.payload['time'] = self.time
                #self.payload['long'] = self.lat
                #self.payload['lat' ] = self.long


   
    def read(self):
        while True:
        # self.inp=ser.readline()
            self.inp = readlineCR().strip()
            if self.inp[:6] =='$GPGGA': # GGA data , packet 1, has all the data we need
                break
            time.sleep(0.1)
        try:
            ind=self.inp.index('$GPGGA',5,len(self.inp))	#Sometimes multiple self data packets come into the stream. Take the data only after the last '$GPGGA' is seen
            self.inp=self.inp[ind:]
        except ValueError:
            print ""
        self.GGA=self.inp.split(",")	#Split the stream into individual parts


    #Split the data into individual elements
    def vals(self):
        self.time=self.GGA[1]
        self.lat=self.GGA[2]
        self.lat_ns=self.GGA[3]
        self.long=self.GGA[4]
        self.long_ew=self.GGA[5]
        self.fix=self.GGA[6]
        self.sats=self.GGA[7]
        self.alt=self.GGA[9]
        return [self.time,self.fix,self.sats,self.alt,self.lat,self.lat_ns,self.long,self.long_ew]
 


if __name__ == '__main__':
  
    client = Client('10.22.66.215', 13000)
