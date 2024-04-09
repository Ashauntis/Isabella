class Animation:
    def __init__(self, images, dur, start_frame=0, loop=True):
        self.dur = dur
        self.images = images

        # record the starting frame of the animation
        self.start_frame = start_frame

        # which frame of our animation to render to the screen
        self.selected_frame_index = self.start_frame

        # how long the animation has been running
        self.frame_count = 0

        # do we loop or stop at the end of the animation?
        self.loop = loop
        self.done = False

    def reset(self):
        # which frame of our animation to render to the screen
        self.selected_frame_index = self.start_frame

        # how long the animation has been running    
        self.frame_count = 0

        self.done = False

    def update(self):
        self.frame_count += 1 
        # print(f"Frame count: {self.frame_count}, Frame Duration: {self.dur}")
        if self.frame_count > self.dur:
            self.frame_count = 0
            self.selected_frame_index += 1
            if self.selected_frame_index >= len(self.images) and not self.loop:
                    self.done = True
        
        # print(f"Current frame: {self.current_frame}, Frame Duration: {self.dur}, Frame count: {self.frame_count}")

    def get_current_image(self):
        return self.images[int(self.selected_frame_index)%len(self.images)]