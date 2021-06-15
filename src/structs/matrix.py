class Matrix:
	def __init__ (self, width, height, default=None):
		self.__default = default
		self.__width, self.__height = width, height
		self.__volume = self.__width * self.__height
		self.__list = [default] * self.__volume

	@property
	def width(self):
		return self.__width

	@property
	def height (self):
		return self.__height

	@property
	def volume (self):
		return self.__volume

	@property
	def default (self):
		return self.__default

	def get (self, row, column):
		index = self.__index (row, column)
		return self.__list [index]

	def row (self, index):
		_index = (index % self.__height) * self.__width
		return self.__list [_index:_index+self.__width]

	def column (self, index):
		_index = index % self.__width
		return self.__list [_index::self.__width]

	def __getitem__ (self, key):
		if isinstance (key, slice):
			start = not (key.start is None)
			stop = not (key.stop is None)
			if start and stop:
				return self.get (key.start, key.stop)
			elif start:
				return self.row (key.start)
			elif stop:
				return self.column (key.stop)
			else:
				return Matrix (
					self.__width,
					self.__height,
					self.__default
				).from_list (self.__list)
		elif isinstance (key, int):
			return self.row (key)
		else:
			raise TypeError ("Unsupported type for matrix slice: " + str (type (key)))

	def __setitem__ (self, key, value):
		if isinstance (key, slice):
			self.set (key.start, key.stop, value)
		else:
			raise TypeError ("Unsupported key for setting: " + str (type (key)))

	def __set (self, row, column, value):
		self.__list [self.__index (row, column)] = value

	def __index (self, row, column):
		# row %= self.__height
		# column %= self.__width
		index = self.__width * (row % self.__height) + (column % self.__width)
		return index

	def set (self, row, column, value=None):
		index = self.__index (row, column)
		if value is None:
			value = self.__default
		self.__list[index] = value
		return self

	def fill (self, value=None):
		if value is None:
			value = self.__default
		for i in range (self.__volume):
			self.__list[i] = value
		return self

	def fill_area (self, y0, x0, height, width, value=None):
		for y in range (y0, y0+height):
			for x in range (x0, x0+width):
				# self.set (y, x, value)
				self.__list[y*self.__width + x] = value

	def area_is_default (self, x0, y0, h, w):
		# for y in range (y0, y0+height):
		# 	for x in range (x0, x0+width):
		# 		if self.__list [y*self.__width+x] != self.__default:
		# 			return False
		return all (item == self.__default for _, __, item in self.get_area (x0, y0, h, w))

	def get_area (self, x0, y0, height, width):
		for y in range (y0, y0+height):
			for x in range (x0, x0+width):
				yield y, x, self.__list[y*self.__width + x]

	def foreach (self):
		for y in range (self.height):
			for x in range (self.width):
				yield y, x, self[y:x]

	def across (self):
		for y in range (self.height):
			for x in range (self.width):
				yield y, x

	def from_2d (self, lst):
		for row in range (len(lst)):
			for column in range (len (lst[row])):
				self.__set (row, column, lst[row][column])
		return self

	def from_list (self, lst):
		if len (lst) != self.__volume:
			raise ValueError ("List length (%d) != matrix volume (%d)" % (len (lst), self.__volume ) )
		for i, v in enumerate (lst):
			self.__list[i] = v
		return self

	def rows (self):
		for y in range (self.__height):
			yield self.row (y)

	def columns (self):
		for x in range (self.__width):
			yield self.column (x)


	@classmethod
	def square (cls, size, default=None):
		return cls (size, size, default)