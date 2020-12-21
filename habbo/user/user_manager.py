import scuti
import habbo.user.user
import util.logging as log


class UserManager:
    def __init__(self):
        self.users = {}
        self.clients = {}

    def add_user(self, user):
        if user.id not in self.users:
            self.users[user.id] = user
        else:
            log.error("Cannot add this user to the users collection")

    def add_client(self):
        pass

    def load_users(self):
        req_rooms = scuti.db.query("SELECT * FROM users", "")
        for req_room in req_rooms:
            self.add_user(habbo.user.user.User(req_room))

    def is_valid_user(self, username):
        for user in self.users.values():
            if user.username == username:
                return True
        return False
