import os

from utils import inside

class Enum:
	def __init__ (self, offset=255):
		self.__names = list ()
		self.__offset = offset


	def get (self, name: str) -> int:
		"""If name is already in registry - returns it's code;
		else creates a new entry and returns it's code

		:param name: the desired name
		:return: the code of this name
		"""
		if name in self.__names:
			return self.__names.index (name) + self.__offset
		return self.encode (name) + self.__offset

	def encode (self, name: str) -> int:
		"""Creates a new entry in registry

		:param name: the desired name to be encoded
		:return: the code of new entry
		"""
		self.__names.append (name)
		return len (self.__names) - 1

	def decode (self, signature:int):
		index = inside (self.__names, abs(signature) - self.__offset)
		return self.__names[index]

	def loads (self, s: str):
		"""
		Load names from a string and calls self.get () for everyone

		:param s: a string with names
		:return:
		"""
		names = self.truncate (s)
		for name in names:
			self.get (name)


	def load (self, path: str) -> bool:
		if os.path.isfile (path):
			with open (path) as file:
				data = file.read ()
				names = self.truncate (data)
				for name in names:
					self.get (name)
			return True
		return False

	def dump (self, path: str, rewrite=False) -> bool:
		if (os.path.exists (path) and rewrite) or not rewrite:
			with open (path, 'w') as file:
				file.writelines(self.__names)
			return True
		return False

	@staticmethod
	def trim (s: str) -> str:
		processed = s.lower ().strip ().rstrip ()
		return processed

	@staticmethod
	def truncate (s: str):
		processed = s.strip ().rstrip ().lower ().replace ('\n', ' ').split ()
		return processed

	# def __call__ (self, name: str):
	# 	return self.get (name)
	__call__ = get

	@property
	def len (self):
		return len (self.__names) + self.__offset

	@property
	def names (self):
		for name in self.__names:
			yield name