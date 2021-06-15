from component import COMPONENT_LIST

class ComponentMaster:
	def __init__(self):
		self.__components = [c for c in COMPONENT_LIST]

	def getid (self, component_type):
		return self.__components.index (component_type)

	def get_component (self, uid):
		return self.__components[uid]

	def components (self):
		yield from self.__components