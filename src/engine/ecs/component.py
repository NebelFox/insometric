from structs.vectors import Vector
from dataclasses import dataclass
from pygame import Surface, Rect
from entity import Entity
from engine.graphics import SpriteSheet

@dataclass
class Transform:
	position: Vector
	rotation: int = 0
	scale: Vector = Vector (1, 1)

@dataclass
class RigidBody:
	velocity: Vector = Vector (0, 0)

# @dataclass
# class Sprite:
# 	image: Surface
# 	z: float = 0.0
# 	visible: bool = True

@dataclass
class Sprite:
	image: Surface
	z: float = 0.0

class Animator:
	def __init__ (self, *sheets, duration=1):
		self.sheets = {i:sheet for i, sheet in enumerate (sheets)}
		self.state = 0
		self.frame = 0
		self.duration = duration

@dataclass
class BoxCollider:
	body: Rect

@dataclass
class Parent:
	children: list[Entity]

COMPONENT_LIST = [
	Transform,
	RigidBody,
	Sprite,
	BoxCollider,
	Parent
]

COMPONENT_COUNT = len (COMPONENT_LIST)