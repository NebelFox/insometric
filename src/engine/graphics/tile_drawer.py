import config as cfg
import pygame
import runtime
from random import choice

class TileDrawer:
	def __init__ (self, matrix, tiles):
		self.size = cfg.tile.size
		self.surface: pygame.surface.Surface = runtime.surface
		self.tiles = tiles
		self.matrix = matrix
		self.prefab = pygame.surface.Surface (cfg.display.size)
		for y, x, index in self.matrix.foreach ():
			# print (self.matrix[y:x])
			tile = self.tiles[index]
			rect = self.ceil (x, y)
			self.prefab.blit (choice (tile.images), rect)

	def ceil (self, x, y):
		return pygame.rect.Rect (x*self.size, y*self.size, self.size, self.size)

	def draw (self, x, y):
		rect = self.ceil (x, y)
		self.surface.blit (self.prefab, rect, rect)

	def draw_all (self):
		self.surface.blit (self.prefab, (0, 0))