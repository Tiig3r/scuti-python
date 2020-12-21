import util.logging as log
from communication.incoming.incoming import UserLoginEvent
from communication.incoming.user.login import UserLoginEvent


class MessageHandler:
    def __init__(self):
        self.events = {
            UserLoginEvent: UserLoginEvent,
        }

    def incoming_message(self, client, message_id, message):
        if message is not None:
            if message_id in self.events:
                log.line("[PACKET] " + message_id + " : waiting...")
                try:
                    self.events[message_id].handle()
                except Exception as e:
                    log.line("[PACKET] " + message_id + " : doesn't work!")
                    log.line()
                    log.error(str(e))
            else:
                log.error("This packet id is not registered!")

