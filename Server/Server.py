# -*- coding: utf-8 -*-
import SocketServer
import json
import datetime
import re
import time
import os
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

users = []
online = {}
history = []
# banned = {}


def fill_response(username, response, content):
    return {
        'timestamp': datetime.datetime.fromtimestamp(
            time.time()).strftime('%H:%M:%S'),
        'sender': username,
        'response': response,
        'content': content,
    }


def handle_login(username):

    if username in online:
        print "username already in logged in"
        return fill_response('server', 'error', 'Already logged in!'), False
    elif username == '':
        return fill_response('server', 'error', 'Empty username!'), False
    elif len(username) > 12:
        return fill_response('server', 'error', 'Too long username!'), False
    else:
        # http://stackoverflow.com/questions/13353663/what-is-the-regular-expression-to-allow-uppercase-or-lowercase-alphabetical-char
        if re.match("[A-Za-z0-9\s]+$", username):
            return fill_response('server', 'info', 'Login succsesful!'), True
        else:
            return fill_response('server', 'error', 'Invalid username!'), False


def handle_logout(username):
    if username in users:
        return fill_response('server', 'info', "you've logged out!"), True
    else:
        return fill_response('server', 'error', "you're not logged in!"), False


def handle_msg(username, msg):
    if username in users:
        return fill_response(username, 'message', msg), True
    else:
        return fill_response('server', 'error', "you're not logged in!"), False


def handle_names(username):
    names = ""
    if username in users:
        for user in online:
            names += user + ", "
        return fill_response('server', 'info', names)
    else:
        return fill_response('server', 'error', "you're not logged in!")


def handle_help():
    text = """Available requests:
        login <username> | logout | msg <message> | names | help\n\t
        Username can only be letters and numbers, shorter than 12 in length!"""

    return fill_response('server', 'info', text)


class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        self.name = ''
        self.login = False
        broadcast_flag = False
        print '  |  <New client> ', self.ip, ':', str(self.port), ' |'
        print '  *-----------------------------------*'
        global users
        global online
        global history

    # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)

            if received_string:
                # TODO: Add handling of received payload from client
                received = json.loads(received_string)
                request = received['request']
                content = received['content']

                if request == 'login':
                    if self.login:
                        response = fill_response(
                            'server', 'error', "You're already logged in!")
                        status = True
                    else:
                        response, status = handle_login(content)
                    if status:
                        self.name = content
                        self.login = True
                        users.append(content)
                        online[self.name] = self
                        if len(history) > 0:
                            self.connection.sendall(
                                json.dumps(response).encode('utf-8'))
                            time.sleep(1)
                            response = fill_response(
                                'server', 'history', history)

                elif request == 'logout':
                    response, status = handle_logout(self.name)
                    self.login = False
                    if status:
                        del online[self.name]
                        self.connection.sendall(
                            json.dumps(response).encode('utf-8'))
                        self.finish()

                elif request == 'msg':
                    response, status = handle_msg(self.name, content)
                    if status:
                        broadcast_flag = True
                        history.append(json.dumps(response))

                elif request == 'names':
                    response = handle_names(self.name)

                elif request == 'help':
                    response = handle_help()

                else:
                    response = fill_response(
                        'server', 'error', 'Undefined request')

                if broadcast_flag:
                    broadcast_flag = False
                    for user in online:
                        online[user].connection.sendall(
                            json.dumps(response).encode('utf-8'))
                else:
                    self.connection.sendall(
                        json.dumps(response).encode('utf-8'))
            else:
                if self.name in online:
                    del online[self.name]
                self.login = False
                print '  |  <Disconnect> ', self.ip, ':', str(self.port), ' |'
                print '  *-----------------------------------*'
                break


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
    HOST, PORT = '0.0.0.0', 13000
    os.system("clear")
    print '\n  *------------------*'
    print '  | ' '\x1b[1;1;33m', 'Server running', '\x1b[0m', '|'
    print '  *-----------------------------------*'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
