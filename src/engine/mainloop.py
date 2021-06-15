import runtime
import config as cfg
from .timer import Timer
class Mainloop:

	def __init__ (self):
		self.__state = 0
		self.fps = cfg.display.fps
		self.stream = runtime.stream
		self.clock = runtime.clock
		self.object_drawer = runtime.object_drawer

	def run (self):
		if self.__state == 2:
			raise RuntimeError ("Mainloop is already running")
		self.__state = 2
		while self.__state > 0:
			self.update ()

	def stop (self):
		if self.__state == 0:
			raise RuntimeError ("Mainloop is already dead")
		self.__state = 0

	def pause (self):
		if self.__state != 2:
			raise RuntimeError ("Mainloop should be running while pausing")
		self.__state = 1

	def resume (self):
		if self.__state != 1:
			raise RuntimeError ("Mainloop needs to be paused before resuming")
		self.__state = 2

	def update (self):
		if self.__state == 2:
			self.clock.tick (self.fps)
			Timer.update ()
			self.stream.update ()
			self.object_drawer.update ()