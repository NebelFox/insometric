import pygame
import runtime
from time import time
import config as cfg

class FPS (pygame.sprite.Sprite):
	def __init__ (self, *groups):
		pygame.sprite.Sprite.__init__ (self, *groups)
		font_name = pygame.font.match_font ('arial')
		font_size = cfg.fps.font_size
		self.font = pygame.font.Font (font_name, font_size)

		height = int (font_size * 1.3)
		width = int (font_size * 4)
		alignx, aligny = cfg.fps.alignx, cfg.fps.aligny
		x = cfg.display.centerx * (alignx+1) - (width//2) * alignx
		y = cfg.display.centery * (aligny+1) - (height//2) * aligny
		self.rect = pygame.rect.Rect (0, 0, width, height)
		self.rect.center = (x, y)
		self.bg_image = pygame.surface.Surface (self.rect.size)
		self.bg_image.fill ((0, 0, 0))

		self.color = (255, 255, 255)

		self.last_update = time ()
		self.fps = cfg.display.fps
		self.text = ''
		self.render ()
		self.counter = self.max_counter = 6

	def update (self, surface):
		self.counter -= 1
		if self.counter <= 0:
			self.counter = self.max_counter
			now = time ()
			delta = (now - self.last_update)/self.max_counter
			self.last_update = now
			self.fps = round (1/delta)
			self.render ()
		surface.blit (self.bg_image, self.rect)
		surface.blit (self.text, self.rect)

	def render (self):
		self.text = self.font.render ("FPS: " + str (self.fps), True, self.color)