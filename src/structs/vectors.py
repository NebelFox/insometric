from math import floor, ceil, atan2, sqrt, sin, cos, radians, trunc
from typing import Union
from src.utils import overload
scalar = Union[int, float]


class Vector:
	def __init__ (self, x:scalar, y:scalar):
		self.x = float (x)
		self.y = float (y)

	def tuple (self):
		return self.x, self.y

	def direction (self):
		return atan2 (self.y, self.x)

	def length (self):
		if not self.x*self.y:
			return abs(self.x + self.y)
		else:
			return sqrt (self.x*self.x + self.y*self.y)

	def __iadd__ (self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __add__ (self, other):
		return Vector (self.x + other.x, self.y + other.y)

	def __imul__(self, other:scalar):
		self.x *= other
		self.y *= other
		return self

	def __mul__ (self, other):
		return self.x * other.x + self.y * other.y

	def __rmul__ (self, other):
		return Vector (self.x * other, self.y * other)

	def __idiv__ (self, other:float):
		self.x /= other
		self.y /= other
		return self

	def __div__ (self, other):
		return Vector (self.x / other, self.y / other)

	def __floordiv__ (self, other):
		return Vector (self.x // other, self.y // other)

	def __divmod__ (self, other):
		return Vector (self.x % other, self.y % other)

	def __repr__ (self):
		return "Vector (" + str (round (self.x, 4)) + ", " + str (round (self.y, 4)) + ")"

	def floor (self):
		return Vector (floor (self.x), floor (self.y))

	def ceil (self):
		return Vector (ceil (self.x), ceil(self.y))

	def trunc (self):
		return Vector (trunc (self.x), trunc (self.y))

	def copy (self):
		return Vector (self.x, self.y)

	def scale (self, other):
		return round(
			self.length () * other.length () * cos (
				abs (self.direction () - other.direction ())
			),
			10
		)

	@overload (float)
	def rotate (self, delta: float):
		l = self.length ()
		d = self.direction ()
		self.x = cos (d + delta) * l
		self.y = sin (d + delta) * l

	@overload (int)
	def rotate (self, degree:int):
		self.rotate (radians (degree))

	@overload (float)
	def set_rotation (self, alpha):
		l = self.length ()
		self.x = cos (alpha) * l
		self.y = sin (alpha) * l

	@overload (int)
	def set_rotation (self, alpha):
		self.set_rotation (radians (alpha))

	@classmethod
	def up (cls):
		return cls (0, -1)

	@classmethod
	def down (cls):
		return cls (0, 1)

	@classmethod
	def left (cls):
		return cls (-1, 0)

	@classmethod
	def right (cls):
		return cls (1, 0)

	@classmethod
	def zero (cls):
		return cls (0, 0)

	@classmethod
	def one (cls):
		return cls (1, 1)

	def __bool__(self):
		return self.x != 0 and self.y != 0

	def __eq__ (self, other):
		return self.x == other.x and self.y == other.y

	def __ne__ (self, other):
		return self.x != other.x or self.y != other.y

	def __lt__ (self, other):
		return self.x < other.x and self.y < other.y

	def __gt__ (self, other):
		return self.x > other.x and self.y > other.y

	def __le__(self, other):
		return self.x <= other.x and self.y <= other.y

	def __ge__(self, other):
		return self.x >= other.x and self.y >= other.y

	def __invert__ (self):
		return Vector (self.y, self.x)

	def __neg__ (self):
		return Vector (-self.x, -self.y)

	def __abs__ (self):
		return Vector (abs (self.x), abs (self.y))

	def __round__ (self, n=None):
		return Vector (round (self.x, n), round (self.y, n))

class Vector3:
	def __init__ (self, x:scalar, y:scalar, z:scalar):
		self.x = float (x)
		self.y = float (y)
		self.z = float (z)

	def tuple (self):
		return self.x, self.y, self.z

	# def direction (self):
	# 	return atan2 (self.y, self.x)

	def length (self):
		return sqrt (self.x*self.x + self.y*self.y + self.z*self.z)

	def __iadd__ (self, other):
		self.x += other.x
		self.y += other.y
		self.z += other.z
		return self

	def __add__ (self, other):
		return Vector (self.x + other.x, self.y + other.y, self.z + other.z)

	def __imul__(self, other:scalar):
		self.x *= other
		self.y *= other
		self.z *= other
		return self

	def __mul__ (self, other):
		return self.x * other.x + self.y * other.y + self.z * other.z

	def __rmul__ (self, other):
		return Vector3 (self.x * other, self.y * other, self.z * other)

	def __idiv__ (self, other:float):
		self.x /= other
		self.y /= other
		self.z /= other
		return self

	def __div__ (self, other):
		return Vector3 (self.x / other, self.y / other, self.z / other)

	def __floordiv__ (self, other):
		return Vector3 (self.x // other, self.y // other, self.z // other)

	def __divmod__ (self, other):
		return Vector3 (self.x % other, self.y % other, self.z % other)

	def __repr__ (self):
		return "Vector ({}, {}, {})".format (
			round (self.x, 4),
			round (self.y, 4),
			round (self.z, 4)
		)

	def floor (self):
		return Vector3 (floor (self.x), floor (self.y), floor (self.z))

	def ceil (self):
		return Vector3 (ceil (self.x), ceil(self.y), ceil (self.z))

	def copy (self):
		return Vector3 (self.x, self.y, self.z)

	# def scale (self, other):
	# 	return round(
	# 		self.length () * other.length () * cos (
	# 			abs (self.direction () - other.direction ())
	# 		),
	# 		10
	# 	)

	# @overload (float)
	# def rotate (self, delta: float):
	# 	l = self.length ()
	# 	d = self.direction ()
	# 	self.x = cos (d + delta) * l
	# 	self.y = sin (d + delta) * l

	# @overload (int)
	# def rotate (self, degree:int):
	# 	self.rotate (radians (degree))

	# @overload (float)
	# def set_rotation (self, alpha):
	# 	l = self.length ()
	# 	self.x = cos (alpha) * l
	# 	self.y = sin (alpha) * l

	# @overload (int)
	# def set_rotation (self, alpha):
	# 	self.set_rotation (radians (alpha))

	# @classmethod
	# def up (cls):
	# 	return cls (0, -1)
	#
	# @classmethod
	# def down (cls):
	# 	return cls (0, 1)
	#
	# @classmethod
	# def left (cls):
	# 	return cls (-1, 0)
	#
	# @classmethod
	# def right (cls):
	# 	return cls (1, 0)

	@classmethod
	def zero (cls):
		return cls (0, 0, 0)