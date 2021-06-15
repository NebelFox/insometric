from entity import Entity

class EntityMaster:
	def __init__ (self, max_id):
		self.__entities = []
		self.__ids = list (range (max_id))
		self.__id_index = {}
		# self.__index_id = {}
		# self.__length = 0

	def new (self):
		uid = self.__ids.pop ()
		entity = Entity (uid)
		self.__entities.append (entity)
		self.__id_index[uid] = len (self.__entities)
		return entity

	def delete (self, uid):
		index = self.__id_index[uid]
		entity = self.__entities[index]
		entity.destroy ()
		del self.__id_index [uid]
		self.__ids.append (uid)
		self.__entities[index] = self.__entities.pop ()
		self.__id_index[self.__entities[index].id ()] = index

	@property
	def length (self):
		return len (self.__entities)

	def entities (self):
		yield from self.__entities