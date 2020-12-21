import scuti

from network.server import Server
from SimpleWebSocketServer import SimpleWebSocketServer
import util.logging as log
from database.connection import Database
import manager


log.line("#####################")
log.line("#                   #")
log.line("#   Scuti  Server   #")
log.line("#                   #")
log.line("#####################")


scuti.clients = {}
try:
    scuti.db = Database("localhost", "root", "", "scuti")
    log.info("Connected to database!")
    # Room
    manager.room.load_rooms()
    log.info("Room manager loaded!")
    # Users
    manager.user.load_users()
    log.info("User manager loaded!")
except Exception as e:
    log.error(str(e))
    exit()


log.line()
log.info("Server online!")
server = SimpleWebSocketServer("", 3000, Server)
server.serveforever()
