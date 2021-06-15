from component_master import ComponentMaster
from entity_master import EntityMaster
from system_master import SystemMaster

class ECSMaster:
	def __init__ (self):
		self.__component_master = ComponentMaster ()
		self.__entity_master = EntityMaster (1024)
		self.__system_master = SystemMaster ()
		self.get_entities = self.__entity_master.entities
		self.components = self.__component_master.components

	def register_system (self, system):
		self.__system_master.register (system)

	def component_id (self, component_type):
		return self.__component_master.getid (component_type)

	def get_component (self, uid):
		return self.__component_master.get_component (uid)

	def update_systems (self):
		self.__system_master.update ()

	def new_entity (self):
		return self.__entity_master.new ()

	def delete_entity (self, uid):
		self.__entity_master.delete (uid)

	def entity_count (self):
		return self.__entity_master.length