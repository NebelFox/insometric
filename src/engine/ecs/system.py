from structs import Signature
from component import *
from system_master import SystemMaster
from runtime import surface, component_master, stream
from utils import binary_search

class System:
	def __init__ (self, update_procedure, *requirements):
		self.__targets = set ()
		self.__signature = Signature (
			indices=(component_master.get_id (r) for r in requirements),
			length=COMPONENT_COUNT
		)
		self.__update = update_procedure

	@stream.event
	def on_signature_changed (self, event):
		matches = self.__signature & event.entity.signature
		if matches and not (event.entity in self.__targets):
			self.__targets.add (event.entity)
		elif not matches and (event.entity in self.__targets):
			self.__targets.remove (event.entity)

	def load_entities (self, entities):
		for entity in entities:
			if self.__signature & entity.signature:
				self.__targets.add (entity)

	def update (self):
		for entity in self.__targets:
			self.__update (entity)


system_master = SystemMaster ()

# # render system
# def update (entity):
# 	mesh = entity.get (Sprite)
# 	if mesh.visible:
# 		surface.blit (mesh.image, entity.get (Transform).position.tuple ())
# system_master.register (System (update, Transform, Sprite))

# physics system
def update (entity):
	entity.get (Transform).position += entity.get (RigidBody).velocity
system_master.register (System (update, Transform, RigidBody))

# children system
def update (entity):
	for child in entity.get (Parent).children:
		child.get (Transform).position += entity.get (RigidBody).velocity
system_master.register (System (update, Parent))

class RenderSystem:
	def __init__ (self):
		self.__targets = list ()
		self.__signature = Signature (
			indices=(component_master.get_id (r) for r in (Transform, Sprite)),
			length=COMPONENT_COUNT
		)

	@stream.event
	def on_signature_changed (self, event):
		matches = self.__signature & event.entity.signature
		if matches and not (event.entity in self.__targets):
			self.__targets.insert (binary_search (self.__targets, event.entity.get (Sprite).z, lambda x: x.get (Sprite).z), event.entity)
			# self.__targets.append (event.entity)
		elif not matches and (event.entity in self.__targets):
			self.__targets.remove (event.entity)

	def load_entities (self, entities):
		for entity in entities:
			if self.__signature & entity.signature:
				self.__targets.append (entity)
		self.__targets.sort (lambda e: e.get (Sprite).z)

	def update (self):
		for entity in self.__targets:
			sprite = entity.get (Sprite)
			transform = entity.get (Transform)
			surface.blit (sprite.sprites[sprite.state][sprite.frame], transform.position.tuple ())
			sprite.frame += 1 - (sprite.frame+1 > len(sprite.sprites[sprite.state])-1) * len(sprite.sprites[sprite.state])
