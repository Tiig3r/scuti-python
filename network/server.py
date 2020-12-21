"""
Scuti server
Author: Tig3r
"""
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


class Server(WebSocket):
    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')
