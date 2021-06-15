print ("Event handlers initialization!")
import pygame
from engine import Event

import runtime
stream = runtime.stream
enum = runtime.enum

@stream.event_handler
def quit_handler (event):
	if event.type == pygame.QUIT:
		stream.order (Event('quit'))
		return True

@stream.event_handler
def key_handler (event):
	if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
		stream.order (Event('key').data(state=event.type, key=event.key))
		return True

mouse_states = {
	pygame.MOUSEBUTTONUP: 'up',
	pygame.MOUSEBUTTONDOWN: 'down'
}
@stream.event_handler
def mouse_handler (event):
	if event.type in mouse_states:
		x, y = pygame.mouse.get_pos ()
		state = mouse_states[event.type]
		stream.order (Event ('mouse').data (state=state, x=x, y=y))

	# if event.type == pygame.MOUSEBUTTONDOWN:
	# 	stream.order (Event ('mouse').data (state='down', pos=pygame.mouse.get_pos ()))
	# elif event.type == pygame.MOUSEBUTTONUP:
	# 	stream.order (Event ('mouse').data (state='up', pos=pygame.mouse.get_pos ()))