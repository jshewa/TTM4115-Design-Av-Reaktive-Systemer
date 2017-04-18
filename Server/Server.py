__author__ = 'Jakob'


__author__ = 'Jakob'
import socket
import json

class Server():

    def __init__(self,port):
        self.id = 1
        self.pieSocket = socket.socket()
        self.ip=socket.gethostname()
        print(self.ip)
        self.port=port
        address = (self.ip,port)
        self.pieSocket.bind(address)
        self.pieSocket.listen(1)

        self.appSocket = socket.socket()
        self.port1=port+1
        address2 = (self.ip,self.port1)
        self.appSocket.bind(address2)
        self.appSocket.listen(1)



    def run(self):
        print("Startet listening on " + self.ip + "," + str(self.port))
        while True:
            try:
                conn,addr = self.pieSocket.accept()
                received_string = conn.recv(4096)
                received_json = json.loads(received_string.decode('utf-8'))
                print(received_json)
                id = received_json['id']

                #Autorisering, men den er hardkodet :))
                if self.id == id:
                    conn2,addr2 = self.appSocket.accept()
                    conn2.send(json.dumps(str(received_json)).encode('utf-8'))
                else:
                    print("fuck off very much yes")

            except Exception as e:
                print (e.message)
                return

    def get_payloadToPie(signal):
        return {
            "signal": signal,
        }

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






