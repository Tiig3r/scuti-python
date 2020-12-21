"""
Scuti server
Author: Tig3r
"""
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import scuti
import util.logging as log


class Server(WebSocket):
    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        log.line(self.address[0] + " is now connected!")

    def handleClose(self):
        log.line(self.address[0] + " is disconnected!")
