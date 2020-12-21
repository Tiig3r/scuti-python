"""
Scuti server
Author: Tig3r
"""
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import scuti
import util.logging as log
from manager import message_handler
import json


class Server(WebSocket):
    def handleMessage(self):
        packet = json.loads(self.data)
        id = packet["packetId"]
        data = packet["data"]
        # Debug
        message_handler.incoming_message(self, id, data)

    def handleConnected(self):
        log.line(self.address[0] + " is now connected!")

    def handleClose(self):
        log.line(self.address[0] + " is disconnected!")
