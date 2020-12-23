import json


class MessageComposer:
    def __init__(self):
        self.packet = {}

    def write(self, key, value):
        self.packet[key] = value

    def compose(self):
        return json.dumps(self.packet)
