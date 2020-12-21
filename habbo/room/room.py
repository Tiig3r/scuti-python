class Room:
    def __init__(self, req):
        self.id = req[0]
        self.owner_id = req[1]
        self.owner_name = req[2]
        self.name = req[3]
        self.description = req[4]
        self.users_max = req[5]
        self.password = req[6]
        self.state = req[7]
        self.wall_thickness = req[8]
        self.wall_height = req[9]
        self.floor_thickness = req[10]
        self.floor = req[11]

    def get_id(self):
        return self.id

    def get_owner_id(self):
        return self.owner_id

    def get_owner_name(self):
        return self.owner_name

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_users_max(self):
        return self.users_max



