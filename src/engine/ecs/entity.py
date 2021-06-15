from structs import Signature
from runtime import component_master
from component import COMPONENT_COUNT

class Entity:
	def __init__ (self, uid):
		self.__id = uid
		self.__components = [None] * COMPONENT_COUNT
		self.__signature = Signature (length=10)

	def get (self, component_type):
		return self.__components[component_master.getid (component_type)]

	def add (self, component):
		component_id = component_master.getid (type (component))
		self.__components[component_id] = component
		self.__signature[component_id] = 1

	def remove (self, component_type):
		component_id = component_master.getid (component_type)
		del self.__components[component_id]
		self.__signature[component_id] = 0

	@property
	def id (self):
		return self.__id

	@property
	def signature (self):
		return self.__signature

	def destroy (self):
		del self.__components
		del self.__signature
		return self.__id

	def components (self):
		yield from self.__components


