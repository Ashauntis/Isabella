import numpy as np
import pygame

class Room:
    def __init__(self, game = None, flags = 0):
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))

        print(f"Room Flags: {flags}")

        room_bits = {
            0b0000_0001: "north",
            0b0000_0010: "east",
            0b0000_0100: "south",
            0b0000_1000: "west",
            0b0001_0000: "start",
            0b0010_0000: "boss",
        }


        self.background = make_transparent_surface((500, 500))
        self.background.fill(("black"))
        self.background_image = load_asset("basement.png")
        # ensure the background image is the same size as the screen
        self.background_image = scale_asset(self.background_image, (500, 500))

        if flags & 0b1111_1111_0000:
            # if room_bits[flags]:
                # self.room_type = room_bits[flags]
            pass
        else:
            self.room_type = "basic"

        self.pickups = []
        self.enemies = []

        self.north = flags & 0b0000_0001
        self.east  = flags & 0b0000_0010
        self.south = flags & 0b0000_0100
        self.west  = flags & 0b0000_1000

    def display_info(self):
        print(f"Room Type: {self.room_type}")
        print(f"North: {self.north}")
        print(f"East: {self.east}")
        print(f"South: {self.south}")
        print(f"West: {self.west}")

    def binary_key(self, flags, key):
        matches = []

        for k, v in key.items():
            if flags & k:
                matches.append(v)
        
        return matches



def make_transparent_surface(size: tuple):
    return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()

def scale_asset(asset, size: tuple):
    return pygame.transform.scale(asset, size)

def load_asset(asset_path: str):
    return pygame.image.load("assets/" + asset_path).convert_alpha()

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


size = 8

example_room = Room(flags=0b0001_0001)

dtype = np.dtype([
        ("flags", np.uint8),  # bit-wise flags
        # create a room object to hold the room data
        ("room", "O"),
    ])

floor_map = np.zeros((size, size), dtype=dtype)

print(f"Room before Initialization: {floor_map[1,2]["room"]}")

floor_map[1,2]["room"] = example_room
print(f"Keys: {example_room.binary_key(0b0001_0001, {
            0b0000_0001: "north",
            0b0000_0010: "east",
            0b0000_0100: "south",
            0b0000_1000: "west",
            0b0001_0000: "start",
            0b0010_0000: "boss",
        })}")

print(f"Room after Initialization and setup: {floor_map[1,2]["room"]}")