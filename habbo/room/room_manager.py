import scuti
import util.logging as log
import habbo.room.room


class RoomManager:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        """
        Add a room to the collection of rooms
        :param room:
        :return:
        """
        if room.id not in self.rooms:
            self.rooms[room.id] = room
        else:
            log.error("Cannot add this room to the rooms collection")

    def load_rooms(self):
        req_rooms = scuti.db.query("SELECT * FROM rooms", "")
        for req_room in req_rooms:
            self.add_room(habbo.room.room.Room(req_room))
