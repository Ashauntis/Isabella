import pygame

class AnimatedSprite:
    def __init__(self, animations, default_animation = "idle", start_frame = 0):
        self.animations = animations
        self.default_animation = default_animation
        self.current_animation = default_animation
        self.animations[self.current_animation].current_frame = start_frame
        self.image = self.animations[self.current_animation].get_current_image()

        # track our sprites horizontal facing direction
        self.h_flip = False

    def update(self):

        # updated our animation
        self.animations[self.current_animation].update()

        # a looping animation should never be "done" so
        # this is a safe check to see if a non-looping animation 
        # completed and we should switch back to the default animation

        if self.animations[self.current_animation].done:
            self.switch_animation(self.default_animation)

        self.image = self.animations[self.current_animation].get_current_image()


        # print(f"Current Animation: {self.current_animation}, Current frame: {self.animations[self.current_animation].current_frame}")

    # Switch to a different animation
    def switch_animation(self, key, frame = 0):
        if key == self.current_animation:
            return
        # check if the animations dict has a key of the given key
        if key in self.animations:
            self.current_animation = key
            self.animations[self.current_animation].reset()
            self.animations[self.current_animation].current_frame = frame   
            self.image = self.animations[self.current_animation].get_current_image()
        else:
            print(f"Could not find animation with key: {key}")
