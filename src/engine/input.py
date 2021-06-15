from structs import Vector
import pygame

class InputBase:
	def __init__ (self, name):
		self.__registry = []
		self.__name = name
		self.__duration = 0

	@staticmethod
	def __validate_key (key_raw):
		return pygame.key.key_code (key_raw) if type (key_raw) is str else key_raw

	def update (self, key_states):
		pass

	def __iadd__ (self, listener):
		self.__registry.append (listener)

class Trigger (InputBase):
	def __init__ (self, name: str, key):
		InputBase.__init__ (self, name)
		self.__key = pygame.key.key_code(key) if type (key) is str else key

	def update (self, key_states):
		self.__duration = self.__duration * key_states[self.__key] + key_states[self.__key]
		for listener in self.__registry:
			listener (self.__duration)

class MultiTrigger (InputBase):
	def __init__ (self, name, keys):
		InputBase.__init__ (self, name)
		self.__keys = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in keys
		)

	def update (self, key_states):
		if any (key_states[key] for key in self.__keys):
			for listener in self.__registry:
				listener ()

class Axis (InputBase):
	def __init__ (self, name, positive_key, negative_key):
		InputBase.__init__ (self, name)
		self.__positive_key = pygame.key.key_code(positive_key)\
			if type (positive_key) is str else positive_key
		self.__negative_key = pygame.key.key_code(negative_key)\
			if type (negative_key) is str else negative_key

	def update (self, key_states):
		value = -key_states[self.__negative_key] + key_states[self.__positive_key]
		for listener in self.__registry:
			listener (value)

class MultiAxis (InputBase):
	def __init__ (self, name, positive_keys, negative_keys):
		InputBase.__init__ (self, name)
		self.__positive_keys = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in positive_keys
		)
		self.__negative_keys = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in negative_keys
		)

	def update (self, key_states):
		value = any (key_states[key] for key in self.__positive_keys) \
		- any (key_states[key] for key in self.__negative_keys)
		for listener in self.__registry:
			listener (value)

class Dpad (InputBase):
	def __init__ (self, name, keys):
		InputBase.__init__ (self, name)
		self.__up = pygame.key.key_code(keys["up"]) if type (keys["up"]) is str else keys["up"]
		self.__down = pygame.key.key_code(keys["down"]) if type (keys["down"]) is str else keys["down"]
		self.__left = pygame.key.key_code(keys["left"]) if type (keys["left"]) is str else keys["left"]
		self.__right = pygame.key.key_code(keys["right"]) if type (keys["right"]) is str else keys["right"]

	def update (self, key_states):
		v = Vector (-key_states[self.__left] + key_states[self.__right], -key_states[self.__up] + key_states[self.__down])
		for listener in self.__registry:
			listener (v)

class MultiDpad (InputBase):
	def __init__ (self, name, keys):
		InputBase.__init__ (self, name)
		self.__up = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in keys["up"]
		)
		self.__down = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in keys["down"]
		)
		self.__left = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in keys["left"]
		)
		self.__right = (
			pygame.key.key_code (key) if type (key) is str else key
			for key in keys["right"]
		)

	def update (self, key_states):
		v = Vector (
			- any (key_states[key] for key in self.__left)
			+ any (key_states[key] for key in self.__right),
			- any (key_states[key] for key in self.__up)
			+ any (key_states[key] for key in self.__down)
		)
		for listener in self.__registry:
			listener (v)

listeners = []

def update ():
	key_states = pygame.key.get_pressed ()
	for listener in listeners:
		listener.update (key_states)