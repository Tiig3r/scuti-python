class User:
    def __init__(self, req):
        self.id = req[0]
        self.username = req[1]
        self.sso = ""
        self.credits = req[3]
        self.pixels = req[4]
        self.diamonds = req[5]

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_sso(self):
        return self.sso

    def get_credits(self):
        return self.credits

    def get_pixels(self):
        return self.pixels

    def get_diamonds(self):
        return self.diamonds

