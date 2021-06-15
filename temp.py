from math import floor
from time import time

# def ray (x0: float, y0: float, x1: float, y1:float):
def ray (x0:int, y0:int, x1:int, y1:int, size:int) -> set:
	start = time ()
	x0, y0, x1, y1 = x0/size, y0/size, x1/size, y1/size
	# print ("Starting time:", start)

	ceils = set ()
	# dx = abs (x1 - x0)
	# dy = abs (y1 - y0)
	dx, dy = x1 - x0, y1 - y0
	if dx < 0:
		x0, y0, x1, y1 = x1, y1, x0, y0
	# if dx < 0 and dy < 0:
	# 	print ("bottom-right --> top-left")
	# 	x0, y0, x1, y1 = x1, y1, x0, y0


	dx, dy = abs (dx), abs (dy)

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
		n += int (float(y1)) - y
		error -= (floor (y0) + 1 - y0) * dx
	else:
		y_inc = -1
		n += y - int (floor (y1))
		error -= (y0 - floor (y0)) * dx

	while n > 0:
		ceils.add ((x, y))
		if error > 0:
			y += y_inc
			error -= dx
		else:
			x += x_inc
			error += dy
		n -= 1
	return ceils
	# end = time ()
	# print (ceils)
	# print ("Ending time:", end)
	# print ("Execution time: {} ms".format ( (end - start)*1000) )

# from src.engine.graphics import SpriteSheet
# sheet = SpriteSheet ('symmetry.png', 8)
# for tile in sheet:
# 	print ("Tile variants:", len (tile))