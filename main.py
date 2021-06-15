from time import time
import pygame

pygame.init ()

from engine import *
import runtime
import config as cfg

stream = EventStream ()
runtime.stream = stream

group = pygame.sprite.Group ()
runtime.group = group

import handlers

clock = pygame.time.Clock ()
runtime.clock = clock

surface = pygame.display.set_mode (cfg.display.size)
runtime.surface = surface
pygame.display.set_caption ("isometric")

object_drawer = graphics.ObjectDrawer ()
runtime.object_drawer = object_drawer

mainloop = Mainloop ()

stream.start ()

# import temp

from objects.player import Player
from objects.projectile import Projectile
from utils.fps import FPS
fps = FPS (group)

player = Player (group)


@stream.event
def on_quit (event: Event):
	mainloop.stop ()
	return True

BLACK = (0, 0, 0)

from utils import weighted_choice
from structs import Matrix, JsonFile
from src.objects.facility import Obstacle
location = 'assets/data/locations/yard.json'
path = 'assets/data/facilities/{}.json'
matrix = Matrix (*cfg.room.size, None)
runtime.matrix = matrix
import debug
def reload ():
	global matrix
	surface.fill (BLACK)
	data = JsonFile (location)
	densities = data['tiles.densities']
	rotability = data['tiles.rotability']

	sheet = graphics.SpriteSheet ('tilesets/jard.png', cfg.tile.origin_size)
	tiles = [graphics.Tile (t, rotability[i]) for i, t in enumerate(sheet.sprites)]
	tilemap = Matrix (*cfg.room.size)
	for y, x in tilemap.across ():
		tilemap[y:x] = weighted_choice (densities)
	tiledrawer = graphics.TileDrawer (tilemap, tiles)
	tiledrawer.draw_all ()
	pygame.display.update ()
	del tiledrawer

	mp = data['map']
	objects = [JsonFile (path.format (obj)) for obj in mp['objects']]
	grid = Matrix (*cfg.room.size, 0).from_2d (list (list (map (int, row.split ())) for row in mp['grid']))
	size = cfg.room.size[0]
	door = cfg.room.door_width
	both = size//2 + door
	size -= 1
	for i in range ((size-door+1)//2):
		grid [0:i] = 1
		grid [0:size-i] = 1
		grid [i:0] = 1
		grid [size-i:0] = 1
		grid [size:i] = 1
		grid [size:size-i] = 1
		grid [i:size] = 1
		grid [size-i:size] = 1
	for y, x, index in grid.foreach ():
		if index != grid.default:
			# if objects[index-1]['durability'] is not None:
			# 	width, height = 1, 1
			# 	dy, dx = 0, 1
			# 	while grid[y+dy:x+dx] == index:
			# 		while grid[y+dy:x+dx] == index:
			# 			dx += 1
			# 			if dx*(dy+1) > width*height:
			# 				width, height = dx, dy+1
			# 		dy += 1
			# 		dx = 0
			# 	if width * height > 2:
			# 		print (x, y, width, height)
			sx, sy = objects[index-1]['size']
			is_outer = any (grid[y+sy:x+dx] != index for dx in range (sx))
			# debug.log (y, x, objects[index-1].name, is_outer)
			object_drawer.add (Obstacle ((x, y), index, objects[index-1], is_outer))
			grid.fill_area (y, x, sy, sx, grid.default)


@stream.event
def on_start (event: Event):
	reload ()

def save ():
	for row in matrix.rows ():
		s = ''.join (map (str, row))
		print (s)
	print ()

key_alias = {
	pygame.K_ESCAPE: mainloop.stop,
	pygame.K_r: reload,
	pygame.K_s: save
}

@stream.event
def on_key (event: Event):
	if event.state == pygame.KEYDOWN:
		key = event.key
		if key in key_alias:
			key_alias[key] ()

mainloop.run ()