# import pygame
import runtime

class ObjectDrawer:
	def __init__ (self):
		self.objects = []
		self.surface = runtime.surface

	def add (self, *objects):
		for obj in objects:
			if obj not in self.objects:
				self.objects.append (obj)

	def remove (self, *objects):
		for obj in objects:
			self.objects.remove (obj)

	def clear (self):
		self.objects.clear ()

	def update (self):
		if self.objects:
			self.objects.sort (key=lambda obj: obj.rect.bottom)
			self.objects = list (filter (self.draw, self.objects))

	def draw (self, obj):
		if obj.alive ():
			# print (obj, obj.dirty)
			if obj.dirty:
				# print (obj)
				obj.draw ()
				obj.dirty = False
			return True
		return False