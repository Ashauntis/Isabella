class Room:
    def __init__(self, game, id, position: tuple, room_type="basic"):
        # create a unique id with a timestamp
        self.game = game
        self.id = id
        self.room_type = room_type
        self.pickups = []
        self.enemies = []
        self.x = position[0]
        self.y = position[1]
        self.connections = {
            "up": {
                "pos": (self.x, self.y - 1),
                "room": None
            },
            "down": {
                "pos": (self.x, self.y + 1),
                "room": None
            },
            "left": {
                "pos": (self.x - 1, self.y),
                "room": None
            },
            "right": {
                "pos": (self.x + 1, self.y),
                "room": None
            }
        }

    def add_connection(self, direction, room):
        self.connections[direction]["room"] = room

    def get_connections(self):
        return self.connections
    
    def get_available_connections(self):
        available = []
        for direction in self.connections:
            if self.connections[direction]["room"] == None:
                available.append(self.connections[direction]["pos"])
        return available
    
    def get_position(self):
        return (self.x, self.y)

    def display_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Room Type: {self.room_type}")
        print(f"Capacity: {self.capacity}")
        print(f"Price: {self.price}")