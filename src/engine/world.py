import config as cfg
from math import floor, atan2, degrees, radians, sqrt

def raycast (x0:int, y0:int, x1:int, y1:int) -> list:
	size = cfg.tile.size
	x0, y0, x1, y1 = x0/size, y0/size, x1/size, y1/size

	ceils = list ()
	# dx, dy = x1 - x0, y1 - y0
	# dy = abs (y1 - y0)
	# dx = x1 - x0
	# if dx < 0:
	# 	x0, y0, x1, y1 = x1, y1, x0, y0
	# dx, dy = abs (dx), abs (dy)
	if x1 < x0:
		x0, y0, x1, y1 = x1, y1, x0, y0
	dx, dy = abs (x1 - x0), abs (y1 - y0)

	x = int (floor (x0))
	y = int (floor (y0))

	n = 1
	x_inc: int
	y_inc: int
	error: float
	if dx == 0:
		x_inc = 0
		error = float ('inf')
	elif x1 > x0:
		x_inc = 1
		n += int (floor(x1)) - x
		error = (floor (x0) + 1 - x0) * dy

	else:
		x_inc = -1
		n += int (floor(x1)) - x
		error = (x0 - floor (x0)) * dy

	if dy == 0:
		y_inc = 0
		error -= float ('inf')
	elif y1 > y0:
		y_inc = 1
		n += int (floor(y1)) - y
		error -= (floor (y0) + 1 - y0) * dx
	else:
		y_inc = -1
		n += y - int (floor (y1))
		error -= (y0 - floor (y0)) * dx

	print (error)

	while n > 0:
		ceils.append ((x, y))
		if error > 0:
			y += y_inc
			error -= dx
		else:
			x += x_inc
			error += dy
		n -= 1
	return ceils

def ceil_hit (raycast_result, objects):
	for ceil in raycast_result:
		if ceil in objects:
			return ceil

def angle (x0, y0, x1, y1):
	a = atan2 (y1-y0, x1 - x0)
	return a

def distance (x0, y0, x1, y1):
	dx, dy = x1 - x0, y1 - y0
	d = sqrt (dx*dx + dy*dy)
	return d