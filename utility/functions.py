import random
import Scenes.room as Room

MAX_FLOOR_SIZE = (20, 20)

def generate_level(game, floor_depth, xl=False, void=False):
    max_rooms = 20
    if xl:
        max_rooms = 45
        
    desired_rooms = constrain(int(3.33 * floor_depth + 5), 0, max_rooms)
    desired_deadends = 5
    if xl: 
        desired_deadends += 1
    if void:
        desired_deadends += 2

    
    

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

level = generate_level(None, 1)
print(level)