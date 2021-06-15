import pygame
import config as cfg
from .util import isequal

class Tile:
	def __init__ (self, image:pygame.surface.Surface, rotable=True):
		self.images = [image]
		if rotable:
			rotate = pygame.transform.rotate
			r1 = rotate (image, 90)
			if not isequal (image, r1):
				self.images.append (r1)
				r2 = rotate (image, 180)
				if not isequal (image, r2):
					self.images.append (r2)
					self.images.append (rotate (r1, 180))
		size = cfg.tile.size
		for i, img in enumerate (self.images):
			self.images[i] = pygame.transform.scale (img, (size, size))

	@property
	def image (self):
		return self.images[0]

	def __len__ (self):
		return len (self.images)