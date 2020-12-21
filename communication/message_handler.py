import util.logging as log
import communication.incoming.incoming
from communication.incoming.user.login import UserLoginEvent


class MessageHandler:
    def __init__(self):
        self.events = {
            communication.incoming.incoming.UserLoginEvent: UserLoginEvent(),
        }

    def incoming_message(self, client, message_id, message_data):
        if message_data is not None:
            if message_id in self.events:
                log.line("[PACKET] " + str(message_id) + " : waiting...")
                try:
                    self.events[message_id].handle(client, message_data)
                    log.line("[PACKET] " + str(message_id) + " : OK!")
                except Exception as e:
                    log.line("[PACKET] " + message_id + " : doesn't work!")
                    log.error(str(e))
            else:
                log.error("This packet id is not registered!")

