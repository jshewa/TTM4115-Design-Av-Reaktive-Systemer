# -*- coding: utf-8 -*-
from threading import Thread
import json


class MessageReceiver(Thread):
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
        super(MessageReceiver, self).__init__()
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

            if Message['response'] == 'History':
                # print Message['content']
                history = Message['content']
                # print history
                # history['test'] = 2
                # print history
                histlen = len(history)
                for msg in range(0, histlen):
                    var = json.loads(str(history[msg]))
                    print "<%s> [%s]: %s" % (var['timestamp'], var['sender'], var['content'])
            else:
                print "<%s> [%s]: %s" % (Message['timestamp'], Message['sender'], Message['content'])

    def check_history(hist):
        history = []
        i = 0
        for msg in hist:
            history[i] = json.loads(hist[msg])
            i += 1
        return history
