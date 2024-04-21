from utility.functions import *
import config.colors as colors

class Room:
    def __init__(self, game = None, flags = 0):
        self.game = game
        self.room_type = None

        # print(f"Room Flags: {flags}")

        room_bits = {
            0b0000_0001: "north",
            0b0000_0010: "east",
            0b0000_0100: "south",
            0b0000_1000: "west",
            0b0001_0000: "start",
            0b0010_0000: "boss",
        }

        self.flags = binary_key(flags, room_bits)
        # print(f"Room Flags: {self.flags}")

        for flag in self.flags:
            if flag == "start":
                self.room_type = "start"
            elif flag == "boss":
                self.room_type = "boss"
            else:
                self.room_type = "basic"

        self.background = make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.BLACK))
        self.background_image = load_asset("basement.png")
        # ensure the background image is the same size as the screen
        self.background_image = scale_asset(self.background_image, (self.game.screen_width, self.game.screen_height))

        self.pickups = []
        self.enemies = []

    def display_info(self):
        print(f"Room Type: {self.room_type}")
        print(f"North: {self.north}")
        print(f"East: {self.east}")
        print(f"South: {self.south}")
        print(f"West: {self.west}")