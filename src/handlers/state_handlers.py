print ("State handlers initialization")

import pygame
from engine import Event

import runtime
stream = runtime.stream

# @stream.state_handler
# def mouse_handler ():
# 	pos = pygame.mouse.get_pos ()
# 	rel = pygame.mouse.get_rel ()
# 	pressed = pygame.mouse.get_pressed (3)
# 	stream.order (Event ('mouse').data (pos=pos, rel=rel, pressed=pressed))

# @stream.state_handler
# def key_handler ():
# 	pressed = pygame.key.get_pressed ()