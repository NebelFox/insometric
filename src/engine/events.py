import pygame
import runtime
class Event:
	_now = pygame.time.get_ticks
	_enum = runtime.enum

	def __init__ (self, name):
		self._code = Event._enum (name)
		# self._lifetime = 1
		self._data = dict ()
		self._time = Event._now ()

	def __getattr__ (self, name):
		return self._data [name]

	# chainable methods
	# def lasts (self, lifetime:int=0):
	# 	self._lifetime = lifetime
	# 	return self

	def data (self, **kwargs):
		self._data.update (kwargs)
		return self

	def __call__ (self, **kwargs):
		return self.data (**kwargs)

	def copy (self):
		e = (Event (self.name)
		     # .lasts (self._lifetime)
		     .data (**self._data)
		)
		e.update_time ()
		return e

	def update_time (self):
		self._time = Event._now ()

	@property
	def name (self):
		return self._enum.decode (self.code)

	@property
	def code (self):
		return self._code

	# @property
	# def lifetime (self):
	# 	return self._lifetime

	@property
	def time (self):
		return self._time

	# lifetime methods
	# def update (self) -> int:
	# 	self._lifetime -= 1
	# 	return self._lifetime

	# def cancel (self):
	# 	self._lifetime = 1