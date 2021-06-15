def isequal (sprite1, sprite2):
	rect = sprite1.get_rect ()
	if rect != sprite2.get_rect ():
		return False
	for y in range (rect.height):
		for x in range (rect.width):
			if sprite1.get_at ((x, y)) != sprite2.get_at ((x, y)):
				return False
	return True