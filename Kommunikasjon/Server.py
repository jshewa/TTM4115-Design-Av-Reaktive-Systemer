# -*- coding: utf-8 -*-
import SocketServer
import json
import datetime
import re
import time
import os
from flask import Flask
from flask import request
"""$ set FLASK_APP=Server.py
     flask run --host=0.0.0.0

 * Running on http://127.0.0.1:5000/"""


app = Flask(__name__)




appdata = {'ID':None, 'LAT': None, 'LONG': None}
ledon=1
def setled(color):
    g=open("ledfile.txt","w")
    g.write(color)
    g.close()
def status():
    g=open("status.txt","r")
    status=g.readline().split("=")[1]
    g.close()
    return status


def setval(latmaks,latmin,langmaks,langmin):
    g=open("perfile.txt","w")
    g.write("latmaks="+latmaks+"\n")
    g.write("latmin="+latmin+"\n")
    g.write("langmaks="+langmaks+"\n")
    g.write("langmin="+langmin+"\n")
    g.close()

@app.route('/',methods = ['GET'])
def signal():
    print("Connected");
    ledon=1
    return 0


@app.route('/sendsignal',methods =['POST'])
def sendsignal():
    color = request.form['color']
    setled(color)
    return "signal has been sent"

@app.route('/setper',methods =['POST'])
def setper():
    lat_maks= request.form['Max_latitude']
    lat_min= request.form['Min_latitude']
    lang_maks= request.form['Max_longitude']
    lang_min= request.form['Min_longitude']
    print lat_maks+lat_min+lang_min+lang_maks
    setval(lat_maks,lat_min,lang_maks,lang_min)
    return "Perimeter SET!"

@app.route('/getstatus', methods =['GET'])
def givestatus():
    if status=='0':
        return "CHILD IS OUTSIDE ALLOWED AREA"
    else:
        return "CHILD IS INSIDE ALLOWED AREA"



class ClientHandler(SocketServer.BaseRequestHandler):

    def updatestatus(self):
        good=1
        g = open("perfile.txt","r")
        latmaks=g.readline().split("=")[1]
        latmin=g.readline().split("=")[1]
        langmaks=g.readline().split("=")[1]
        langmin=g.readline().split("=")[1]
        g.close()

        self.pervalues['lat_maks']=int(latmaks)
        self.pervalues['lat_min']=int(latmin)
        self.pervalues['lang_maks']=int(langmaks)
        self.pervalues['lang_min']=int(langmin)
        
        g= open("status.txt","w")
        if self.appresponse['LAT'] > self.pervalues['lat_maks']:
            good=0
        elif self.appresponse['LAT'] < self.pervalues['lat_min']:
            good=0
        elif self.appresponse['LONG'] > self.pervalues['lang_maks']:
            good=0
        elif self.appresponse['LONG'] < self.pervalues['lang_min']:
            good=0
        if good==0:
            g.write("good=0")
            #self.piresponse['signal']= 'red'
        else:
            g.write("good=1")
            #self.piresponse['signal']= 'green'
        g.close()

        g = open("ledfile.txt","r")
        self.piresponse['signal']=g.readline()
       
        """a = g.readline()
        if a== 'yellow':
            self.piresponse['signal']= yellow"""


        g.close()




    def handle(self):
        #print "start"
        """

        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        self.piresponse = {'signal': None }
        self.appresponse = {'LAT': None, 'LONG': None, 'ID': None}
        self.pervalues = {'lat_maks':None, 'lat_min':None, 'lang_maks':None, 'lang_min':None }

        print '  |  <New client> ', self.ip, ':', str(self.port), ' |'
        print '  *-----------------------------------*'
    # Loop that listens for messages from the client
        while True:




            received_string = self.connection.recv(4096)
            print "new position recieved"

            if received_string:
                print received_string
                received = json.loads(received_string)
                print type(received)
                if received['NAME']=="pi":
                    self.appresponse['ID'] = int(received['ID'])
                    self.appresponse['LAT'] = int(received['LAT'])
                    self.appresponse['LONG'] = int(received['LONG'])
                    self.updatestatus()
                    print self.piresponse
                    print type(self.piresponse)
                    self.connection.sendall(json.dumps(self.piresponse))



        



    #self.connection.sendall(json.dumps(self.response))

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True


if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = '192.168.1.2', 13000
    os.system("clear")
    print '\n  *------------------*'
    print '  | ' '\x1b[1;1;33m', 'Server running', '\x1b[0m', '|'
    print '  *-----------------------------------*'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
