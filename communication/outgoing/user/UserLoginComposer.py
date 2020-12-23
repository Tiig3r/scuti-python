from communication.outgoing.message_composer import MessageComposer
from communication.outgoing.outgoing import UserLoginMessage


class UserLoginComposer(MessageComposer):
    def __init__(self):
        super().__init__()
        self.packet["packetId"] = UserLoginMessage
