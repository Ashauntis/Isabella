from utility.functions import * 
import config.colors as colors

class Room:
    def __init__(self, game, flags = 0):
        self.game = game
        room_bits = {
            0b0001_0000: "start",
            0b0010_0000: "boss",
        }

        # for key, room_type in flag_key.items():
        #     if flags & key:
        #         self.room_type = room_type
        #         break

        self.background = make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.BLACK))
        self.background_image = load_asset("basement.png")
        # ensure the background image is the same size as the screen
        self.background_image = scale_asset(self.background_image, (self.game.screen_width, self.game.screen_height))

        if flags in room_bits:
            self.room_type = room_bits[flags]
        else:
            self.room_type = "basic"

        self.pickups = []
        self.enemies = []

        self.north = flags & 0b0000_0001
        self.east  = flags & 0b0000_0010
        self.south = flags & 0b0000_0100
        self.west  = flags & 0b0000_1000

    def display_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Room Type: {self.room_type}")
        print(f"Capacity: {self.capacity}")
        print(f"Price: {self.price}")