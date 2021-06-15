# import os
import json
from random import random, randint

def extract (pool, keylist, index=0):
	if index < len (keylist) - 1:
		key = keylist[index]
		return extract (pool[key], keylist, index + 1)
	return pool[keylist[index]]

def key_to_index (key, prefixes):
	for prefix in prefixes:
		if key.startswith (prefix):
			key = int (key.strip (prefix))
			break
	return key

class JsonFile:
	global_prefixes = ('$', '&')
	def __init__ (self, path, index_prefixes=None):
		with open (path) as file:
			self.data = json.load(file)
		self.path = path
		self.filename = path.split ('/')[-1]
		self.name = self.filename.split ('.')[0]
		# print (self.path, self.filename, self.name)
		self.format = self.filename.strip (self.name)
		if index_prefixes is None:
			self.prefixes = self.global_prefixes
		else:
			self.prefixes = index_prefixes

	def get (self, path: str, fallback=None, sep='.'):
		keys = tuple (map (lambda key: key_to_index (key, self.prefixes), path.split (sep)) )
		try:
			return extract (self.data, keys)
		except KeyError:
			return fallback

	def __getitem__ (self, key):
		return self.get (key)

class DataParser:
	@staticmethod
	def number (data: dict):
		_type = data['type']
		if _type == 'scalar':
			value = data['value']
		elif _type == 'random-int':
			value = randint (data['min'], data['max'])
		elif _type == 'random-float':
			value = random () * (data['max'] - data['min']) + data['min']
		else:
			raise TypeError ("Unsupported type: '" + _type + "'")
		value *= data.get ('floorMultiplier', 1)
		return value