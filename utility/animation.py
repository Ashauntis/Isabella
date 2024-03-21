class Animation:
    def __init__(self, images, dur, start_frame=0, loop=True):
        self.dur = dur
        self.images = images
        self.current_frame = start_frame
        self.frame_count = 0
        self.loop = loop
        self.done = False

    def reset(self):
        self.current_frame = 0
        self.frame_count = 0
        self.done = False

    def update(self):
        self.frame_count += 1 
        if self.frame_count > self.dur and not self.done:
            self.frame_count = 0
            self.current_frame += 1
            if self.current_frame >= len(self.images):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.done = True
        
        print(f"Current frame: {self.current_frame}, Frame Duration: {self.dur}, Frame count: {self.frame_count}")

    def get_current_image(self):
        return self.images[int(self.current_frame)]