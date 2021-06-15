import random
import functools

def overload (*types):
	def register (function):
		if function.__name__ not in overload.registry:
			@functools.wraps (function)
			def wrapper (self, *args):
				return wrapper.typemap [tuple (arg.__class__ for arg in args)] (self, *args)
			wrapper.typemap = dict ()
			overload.registry[function.__name__] = wrapper
		overload.registry[function.__name__].typemap [types] = function
		return overload.registry[function.__name__]
	return register
overload.registry = {}

def bounds (value, mx, mn=0):
	result = max (mn, min (value, mx))
	return result

def xor (condition1: bool, condition2: bool) -> bool:
	"""
	Either the first condition or the second
	"""
	return condition1 + condition2 == 1

def mxor (amount:int, *conditions) -> bool:
	"""
	:param amount: exactly how many conditions must be true
	:param conditions: sequence of conditions
	:return: amount == number of true conditions
	"""
	amount = bounds (amount, len(conditions)-1)
	result = amount == sum (conditions)
	return result

def few (amount:int, *conditions) -> bool:
	"""
	Returns true if the number of true conditions
	is equal or higher than amount
	"""
	amount = bounds (amount, len (conditions)-1)
	result = sum (conditions) >= amount
	return result

def ixor (amount: int, iterable) -> bool:
	"""
	mxor (), but for iterables,
	that are expensive for unpacking,
	or for generators
	"""
	amount -= sum (iterable)
	return amount == 0

def some (amount:int, iterable) -> bool:
	"""
	few () for iterables
	"""
	amount -= sum (iterable)
	return amount <= 0


def find (predicate, iterable):
	for item in iterable:
		if predicate (item):
			return item

def get (iterable, **attrs):
	for item in iterable:
		for name, value in attrs.items ():
			if getattr (item, name, not value) != value:
				return
		return item

def across (iterable):
	"""
	Equal to 'range (len (iterable))'
	"""
	# yield from range (len (iterable))
	return range (len (iterable))

def backwards (iterable):
	"""
	Equal to 'range ( len (iterable) - 1, -1, -1)
	"""
	# yield from range (len (iterable) - 1, -1, -1)
	return range (len (iterable) - 1, -1, -1)

def insert (iterable, value, pos:int) -> int:
	index = expand (iterable, pos)
	iterable.insert (index, value)
	return index

def inside (iterable, pos:int):
	l = len (iterable)
	index = min (l-1, max (-l, pos))
	return index

def expand (iterable, pos:int):
	l = len (iterable)
	index = min (l, max (-l-1, pos))
	return index

def multisplit (s, *args):
	if not args:
		return s
	elif len (args) == 1:
		return s.split (args[0])

	parts = []
	splitters = [' ', '\n'] if not args else list(set(args))

	splitter, index = '', len (s)+1
	while splitters:
		for i in across (splitters):
			spl = splitters[i]
			pos = s.find (spl)
			if pos == -1:
				# splitters.pop (i)
				splitters[i] = None
			elif pos < index:
				index = pos
				splitter = spl
		splitters = list (filter (lambda sp: not (sp is None), splitters))

		part = s[:index]
		if part: parts.append (part)
		s = s[index+len(splitter):]
		index = len (s) + 1
	return parts

def weighted_choice (data):
	if isinstance (data, dict):
		ceil = sum (data.values ())
		target = random.random () * ceil
		floor = 0
		for value, weight in data.items ():
			floor += weight
			if floor >= target:
				return value
	elif isinstance (data, (list, set, tuple)):
		ceil = sum (data)
		target = random.random () * ceil
		floor = 0
		for value, weight in enumerate (data):
			floor += weight
			if floor >= target:
				return value

def sign (a):
	return -1 + int (a>=0) + int (a>0)

import sys
from types import ModuleType, FunctionType
from gc import get_referents
BLACKLIST = type, ModuleType, FunctionType

def sizeof (obj):
	if isinstance (obj, BLACKLIST):
		raise TypeError ("sizeof () doesn't take argument of type: " + str (type (obj)))
	known_ids = set ()
	size = 0
	objects = [obj]
	while objects:
		need_referents = list ()
		for obj in objects:
			if not isinstance (obj, BLACKLIST) and id(obj) not in known_ids:
				known_ids.add (id (obj))
				size += sys.getsizeof (obj)
				need_referents.append (obj)
		objects = get_referents (*need_referents)
	return size

def convert (number, base):
	rests = []
	while number > 0:
		number, rest = number//base, number%base
		rests.append (rest)
	rests.reverse ()
	return rests

from string import ascii_letters
chars = ascii_letters + '0123456789'
BASE = len (chars)

def timeid (number):
	indexes = convert (number, BASE)
	codes = [chars[int (index)] for index in indexes]
	uid = ''.join (codes)
	return uid

def binary_search (l, value, key):
	left = 0
	right = len (l) - 1
	while right - left > 1:
		pivot = left + (right-left)//2
		if key(l[pivot]) < value:
			left = pivot + 1
		elif key(l[pivot]) > value:
			right = pivot - 1
		else:
			return pivot
	return right