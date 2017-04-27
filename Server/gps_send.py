import json
from threading import Thread

class gpssend(Thread):

    def _init_(self,Server,connection):
        super(gpssend,self)._init_()
        self.daemon = True
        self.connection= connection
        self.Server = Server
        print ("thread started")


    def sendSignalToPie(self,color,conn):
        jsonObject = {"signal": color}
        conn.send(json.dumps(str(jsonObject).encode('utf-8')))

    def run(self):
        self.sendSignalToPie("red",self.connection)

