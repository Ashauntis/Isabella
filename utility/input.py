import pygame
import sys
import config.settings as settings

input_map = {
    "left": [pygame.K_LEFT, pygame.K_a],
    "right": [pygame.K_RIGHT, pygame.K_d],
    "up": [pygame.K_UP, pygame.K_w],
    "down": [pygame.K_DOWN, pygame.K_s],
    "space": [pygame.K_SPACE],
    "return": [pygame.K_RETURN],
}

numbers = [
    pygame.K_0,
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
]

letters = [
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
]

special_chars = [
    pygame.K_SPACE,
    pygame.K_PERIOD,
    pygame.K_COMMA,
    pygame.K_SLASH,
    pygame.K_BACKSPACE,
]

def get_input(game):

    # Handle Keyboard Events
    pressed = []
    just_pressed = []
    joysticks = {}    

    # iterate over our input map and check what keys are pressed
    for input_key, options in input_map.items():
        for key in options:
            if pygame.key.get_pressed()[key]:
                pressed.append(input_key)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            # print(f"Key Down: {event.key}")
            for input, options in input_map.items(): 
                if event.key in input_map[input]:
                    just_pressed.append(input)
                    print(f"Key Down: {game.just_pressed}")
            game.console.log(f"Key Down: {event.key}")

        # Handle Controller Events


        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"Joystick {joy.get_instance_id()} connected")

        if event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[event.instance_id]
            print(f"Joystick {event.instance_id} disconnected")

        if event.type == pygame.JOYBUTTONDOWN:
            just_pressed.append(event.button)

    # Toggle our Debug Setting
    if pygame.K_F11 in just_pressed:
        print(f"Toggling Debug Mode: {settings.DEBUG}")
        settings.DEBUG = not settings.DEBUG

    return pressed, just_pressed, joysticks
