class Signature:
	def __init__ (self, **kwargs):
		if "length" in kwargs:
			self.__signature = str(kwargs.get ("default", 0)) * kwargs["length"]
		elif "pattern" in kwargs:
			self.__signature = kwargs["pattern"]
		elif "indices" in kwargs:
			indices = kwargs["indices"]
			self.__signature = "".join (str(int(i in indices)) for i in range (kwargs.get ("length", max(indices))))

	def __len__ (self):
		return len (self.__signature)

	def __getitem__ (self, key):
		return int(self.__signature[key])

	def __setitem__ (self, key, value):
		self.__signature = self.__signature[:key] + str(value) + self.__signature[key+1:]

	def __and__ (self, other):
		for i in range (len(self)):
			if other[i] and not self[i]:
				return False
		return True