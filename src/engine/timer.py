import pygame
from engine import Event
from utils import timeid

class Timer:
	__instances = list ()
	__now = pygame.time.get_ticks
	def __init__ (self, delay, action, times=1):
		self.__delay = delay
		self.__action = action
		self.__times = times
		self.__origin = Timer.__now ()
		self.__state = 2
		self.__event = Event ('timer') (source=self)
		Timer.__instances.append (self)

	def __update (self, now:int):
		if self.__state == 2 and now - self.__origin >= self.__delay:
			self.__times -= 1
			self.__action (self.__event (left=self.__times))
			self.__state *= self.__times != 0
			self.__origin += self.__delay
		return self.alive

	@property
	def alive (self):
		return self.__state > 0

	def pause (self):
		if not self.alive:
			raise ReferenceError ("This timer is already canceled")
		elif self.__state == 1:
			print ("This times is already paused")
		self.__state = 1

	def resume (self):
		if not self.alive:
			raise ReferenceError ("This timer is already canceled")
		elif self.__state == 2:
			print ("This timer is not paused")
		self.__state = 2

	def cancel (self):
		if not self.alive:
			raise ReferenceError ("This timer is already canceled")
		self.__state = 0

	@staticmethod
	def update ():
		now = Timer.__now ()
		Timer.__instances = list (filter (lambda t: t.__update (now), Timer.__instances))

	@staticmethod
	def cancel_all ():
		for instance in Timer.__instances:
			instance.cancel ()
		Timer.__instances.clear ()