import pygame
from collections import deque as Deque

from .events import Event
from utils import across, insert
import runtime

class EventStream:
	"""
	A class that provides a basic event mechanic
	"""

	def __init__ (self, prefix='on_'):
		"""
		:param prefix: the prefix that should be stripped from function name
		"""
		self.enum = runtime.enum
		self.prefix = prefix

		self.registry = [[] for _ in range (self.enum.len)]
		self.stream = list ()
		self.event_handlers = list ()
		self.state_handlers = list ()

		self.running = False
		self.order (Event ('start'))


	def start (self):
		"""
		Turns on the instance
		"""
		self.running = True

	def stop (self):
		"""
		Turns off the instance
		"""
		self.running = False

	def toggle (self) -> bool:
		"""Toggles the state of instance

		:return: new state
		"""
		self.running = not self.running
		return self.running


	def appoint (self, name:str, action, priority=-1):
		"""Appoints an action to be performed at specific event

		:param name: an event name
		:param action: a function, that takes at least 1 argument - event
		:param priority: order of action to be performed
		"""
		code = self.enum (name)
		if not callable (action):
			action = getattr (action, self.prefix+name)
		insert (self.registry[code], action, priority)

	def process (self, target):
		for name in self.enum.names:
			try:
				action = getattr (target, self.prefix+name)
				self.appoint (name, action)
				print (self.prefix+name + " listener was found")
			except AttributeError:
				continue

	def event (self, func):
		"""
		Decorator, used to appoint functions with event names in their names
		"""
		name = func.__name__.lower ().strip (self.prefix)
		self.appoint (name, func)
		return func

	def on_event (self, name: str):
		"""
		Decorator, used to appoint functions,
		but unlike simple 'event', allows to specify the desired event name manually

		:param name: the name of the event this function should be called at
		"""
		def decor (func):
			self.appoint (name.lower (), func)
			return func
		return decor

	def has_entry (self, name:str, action) -> bool:
		"""
		Checks if an action is already appointed to specified event
		:param name: an event name
		:param action: an action
		:return: whether it is in the registry or not
		"""
		name = self.enum (name)
		return action in self.registry[name]

	def release (self, name:str, action) -> bool:
		"""
		If the action is appointed to specified event,
		then cancels this appointing

		:param name: an event name
		:param action: an action to release
		:return: whether action was released or not
		"""
		name = self.enum (name)
		exists = self.has_entry (name, action)
		if exists:
			self.registry[name].remove (action)
		return exists

	def dissolve_registry (self):
		"""
		Dissolves all entries of the registry
		"""
		for name in across (self.registry):
			self.registry[name].clear ()

	def dissolve_by_name (self, name:str):
		"""
		Dissolves all actions that belong to specified event

		:param name: an event name
		:return: whether some actions were dissolved or not
		"""
		name = self.enum (name)
		if self.registry[name]:
			self.registry[name].clear ()
			return True
		return False

	def dissolve_by_action (self, action) -> bool:
		"""
		Seeks for passed action in the registry.
		Dissolves matched entries

		:return: whether some entries were dissolved
		"""
		success = False
		for name in across (self.registry):
			if action in self.registry[name]:
				self.registry[name].remove (action)
				success = True
		return success

	def add_event_handler (self, handler) -> bool:
		print ("assigning event handler")
		if handler not in self.event_handlers:
			self.event_handlers.append (handler)
			return True
		return False

	def event_handler (self, handler):
		self.add_event_handler (handler)
		return handler

	def remove_event_handler (self, handler) -> bool:
		if handler in self.event_handlers:
			self.event_handlers.remove (handler)
			return True
		return False

	def clear_event_handlers (self):
		self.event_handlers.clear ()

	def add_state_handler (self, handler) -> bool:
		print ("assigning state handler")
		if handler not in self.state_handlers:
			self.state_handlers.append (handler)
			return True
		return False

	def state_handler (self, handler):
		self.add_state_handler (handler)
		return handler

	def remove_state_handler (self, handler) -> bool:
		if handler in self.state_handlers:
			self.state_handlers.remove (handler)
			return True
		return False

	def clear_state_handlers (self):
		self.state_handlers.clear ()

	def update (self):
		if self.running:

			for event in pygame.event.get ():
				for handler in self.event_handlers:
					processed = handler (event)
					if processed:
						break

			for handler in self.state_handlers:
				handler ()

			self.order (Event ('update'))

			for event in self.stream:
				for action in self.registry[event.code]:
					if action (event):
						break
			self.stream.clear ()


	def purify (self):
		self.clear_stream ()
		self.dissolve_registry ()
		self.clear_event_handlers()
		self.clear_state_handlers()

	def order (self, event: Event):
		self.stream.append (event)

	def priority_order (self, event: Event, priority:int=0):
		insert (self.stream, event, priority)

	def clear_stream (self):
		self.stream.clear ()