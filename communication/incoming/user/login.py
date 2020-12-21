import manager


class UserLoginEvent:
    def handle(self, client, message_data):
        if manager.user.is_valid_user(message_data["username"]):
            print("ok enft")

