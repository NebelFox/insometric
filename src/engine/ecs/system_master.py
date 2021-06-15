class SystemMaster:
	def __init__ (self):
		self.__systems = []

	def register (self, system):
		self.__systems.append (system)

	def update (self):
		for system in self.__systems:
			system.update ()