import pygame

class SpriteSheet:
	source_dir = 'assets/textures/{}'
	def __init__ (self, path, size, colorkey=None):
		self.size = size
		self.sheet = pygame.image.load (self.source_dir.format (path)).convert ()
		self.countx = self.sheet.get_width () // self.size
		self.county = self.sheet.get_height () // self.size
		self.sprites = []
		for y in range (self.county):
			for x in range (self.countx):
				self.sprites.append (self._sprite_at (x, y, colorkey))

	def _sprite_at (self, x, y, colorkey=None):
		image = pygame.surface.Surface ((self.size, self.size)).convert ()
		rect = pygame.rect.Rect (self.size*x, self.size*y, self.size, self.size)
		image.blit (self.sheet, (0, 0), rect)
		if colorkey:
			if colorkey == -1:
				colorkey = image.get_at ((0, 0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image

	def __len__ (self):
		return len (self.sprites)

	def __getitem__ (self, key):
		return self.sprites[key]

	def __setitem__ (self, key, value):
		self.sprites[key] = value