class Data:
	def __init__ (self, *args, **kwargs):
		self.set (**kwargs)

	def set (self, **kwargs):
		for key in kwargs:
			self.__setattr__ (key, kwargs[key])