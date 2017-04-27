__author__ = 'Jakob'


__author__ = 'Jakob'
import socket
import json
from gps_send import gpssend
class Server():

    def __init__(self,port):
        self.id = 1
        self.pieSocket = socket.socket()
        self.ip="10.22.66.215"
        self.port=port
        address = (self.ip,port)
        self.pieSocket.bind(address)
        self.pieSocket.listen(1)
        self.payload = {'signal': "red"}
        self.appSocket = socket.socket()
        self.port1=port+1
        address2 = (self.ip,self.port1)
        self.appSocket.bind(address2)
        self.appSocket.listen(1)



    def run(self):
        print("Startet listening on " + self.ip + "," + str(self.port))
        message= 0
        conn,addr = self.pieSocket.accept()
        #conn2,addr2 = self.appSocket.accept()
        while True:
            print ("new lop")
            #self.sendSignalToPie("red",conn)
            conn.send(json.dumps(str(self.payload)).encode('utf-8'))
            #try:
            #received_string = conn.recv(4096)
            #received_json = json.loads(received_string.decode('utf-8'))
            #print(received_json)
            print(message)
            message = message +1
                #id = received_json['id']
                #conn.send(self.sendSignalToPie("green",conn))
                #Autorisering, men den er hardkodet :))
                #if self.id == id:
            #conn2.send(json.dumps(str(received_json)).encode('utf-8'))
            #self.sendMessage(conn)
            print("Message sendt")



            #except Exception as e:
                #print(e.message)
                #return
            #finally:
        conn.close()

    def get_payloadToPie(signal):
        return {
            "signal": signal,
        }


    def sendMessage(self,conn):
        rsp = gpssend(self,conn)
        rsp.start()

    def get_payloadToApp(id, time, long, lat):
        return {
            "id": id,
            "time": time,
            "long": long,
            "lat": lat,
        }

    def sendSignalToPie(self,color,conn):
        jsonObject = self.get_payloadToPie()
        conn.send(json.dumps(str(jsonObject).encode('utf-8')))



if __name__ == '__main__':

    server = Server(13000)
    server.run()






