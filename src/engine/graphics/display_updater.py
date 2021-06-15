import pygame
import config as cfg
from structs.matrix import Matrix
from math import floor, ceil

class DisplayUpdater:
	def __init__ (self):
		self.rects = list ()
		self.ceils = Matrix (cfg.room.width, cfg.room.height, 0)
		self.size = cfg.tile.size
		self.width, self.height = cfg.room.size

	def update (self):
		pygame.display.update (self.rects)
		self.rects.clear ()
		self.ceils.fill ()

	def order_all (self):
		self.rects.clear ()
		self.ceils.fill ()
		pygame.display.update ()

	def ceil (self, x, y):
		self.hline (x, y, 1)

	# def order (self, x, y):
	# 	if (x, y) not in self.ceils:
	# 		rect = pygame.Rect (x*self.size, y*self.size, self.size, self.size)
	# 		self.rects.append (rect)
	# 		self.ceils[y:x] = True

	def hline (self, x, y, l):
		if l <= 0:
			return
		valid_len = 0
		for i in range (l):
			if not self.ceils[y:x]:
				valid_len += 1
			elif valid_len > 0:
				self.order_hline (x+i, y, valid_len)
				valid_len = 0
		if valid_len > 0:
			self.order_hline (x + i, y, valid_len)

	def vline (self, x, y, l):
		if l <= 0:
			return
		valid_len = 0
		for i in range (l):
			if not self.ceils[y+i:x]:
				valid_len += 1
			elif valid_len > 0:
				self.order_vline (x, y+i, valid_len)
				valid_len = 0
		if valid_len > 0:
			self.order_vline (x, y + i, valid_len)

	def order_area (self, x, y, w, h):
		for i in range (y, y+h):
			for j in range (x, x+w):
				self.ceils[i:j] = 1
		size = cfg.tile.size
		rect = pygame.Rect (size*x, size*y, size*w, size*h)
		self.rects.append (rect)

	def order_hline (self, x, y, l):
		for i in range (x, x+l):
			self.ceils[y:i] = 1
		size = cfg.tile.size
		rect = pygame.Rect (size*x, size*y, size*l, size)
		self.rects.append (rect)

	def order_vline (self, x, y, l):
		for i in range (y, y+l):
			self.ceils[i:x] = 1
		size = cfg.tile.size
		rect = pygame.Rect (size*x, size*y, size, size*l)
		self.rects.append (rect)

	def area (self, x:int, y:int, w:int, h:int):
		valid_lines = 0
		for i in range (y, y+h):
			ordered_in_line = sum (self.ceils[i:j] for j in range (x, x+w))

			# the whole 'i' line was empty
			if ordered_in_line == 0:
				valid_lines += 1

			# the whole 'i' line was full
			elif ordered_in_line >= w:
				# 'valid_lines' previous lines were empty
				if valid_lines > 0:
					self.order_area (x, i-valid_lines, w, valid_lines)
					valid_lines = 0

			# there were some gaps in 'i' line
			else:
				self.hline (x, y, w)

	def rect (self, r):
		size = cfg.tile.size
		x, y = floor (r.left/size), floor (r.top/size)
		w, h = ceil (r.width/size), ceil (r.height/size)
		self.area (x, y, w, h)

	def movement (self, rect_from, rect_to):
		if rect_from != rect_to:
			self.rect (rect_from)
			self.rect (rect_to)