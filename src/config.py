import configparser
from src.structs import Data, Vector

class Config (configparser.ConfigParser):
	__getters = {
		'i': lambda c, s, o: c.getint (s, o),
		'f': lambda c, s, o: c.getfloat (s, o),
		'b': lambda c, s, o: c.getboolean (s, o),
	}
	__default = lambda c, s, o: c.get (s, o)
	def __call__ (self, path, sep='.'):
		section, option = path.split (sep)
		print (section, option)
		prefix = option[0]
		getter = Config.__getters.get (prefix, Config.__default)
		return getter (self, section, option)

# config = configparser.ConfigParser (interpolation=configparser.ExtendedInterpolation ())
# config.read ('config.ini')
config = Config ()
config.read ('config.ini')

# game = Data (language=config ('game.sLanguage'))
game = Data ()
game.language = config ('game.sLanguage')

# tile = Data (origin_size=config ('tile.iSize'))
tile = Data ()
tile.origin_size = config ('tile.iSize')

# room = Data (
# 	width=config ('room.iWidth'),
# 	height=config ('room.iHeight')
# )
room = Data ()
room.width = config ('room.iWidth')
room.height = config ('room.iHeight')
room.size = (room.width, room.height)
room.door_width = config ('room.iDoorWidth')
# class display:
# 	fps = config ('display.iFps')
# 	scale = config ('display.iScale')
# 	width = tile.origin_size * scale * room.width
# 	height = tile.origin_size * scale * room.height
# 	center = centerx, centery = width // 2, height // 2
# 	size = (width, height)
# display = Data (
# 	fps=config ('display.iFps'),
# 	scale=config ('display.iScale')
# )
display = Data ()
display.fps = config ('display.iFps')
display.scale = config ('display.iScale')
tile.size = tile.origin_size * display.scale
display.width = tile.size * room.width
display.height = tile.size * room.height
display.size = (display.width, display.height)

display.left = -display.width // 2
display.right = display.width // 2
display.top = -display.height // 2
display.bottom = display.height // 2

display.topleft = Vector (display.left, display.top)
display.midtop = Vector (0, display.top)
display.topright = Vector (display.right, display.top)
display.midleft = Vector (display.left, 0)
display.midright = Vector (display.right, 0)
display.bottomleft = Vector (display.left, display.bottom)
display.midbottom = Vector (0, display.bottom)
display.bottomright = Vector (display.right, display.bottom)

display.center = Vector (0, 0)

minimap = Data ()
minimap.room_size = config ('minimap.iRoomSize')

# projectile = Data (
# 	velocity=config ('projectile.fVelocity'),
# 	radius=config ('projectile.iRadius')
# )
projectile = Data ()
projectile.velocity = config ('projectile.fVelocity')
projectile.radius = config ('projectile.iRadius')

# player = Data (
# 	velocity=config ('player.fVelocity'),
# 	speed_steps=config ('player.iSpeedSteps')
# )
player = Data ()
player.velocity = config ('player.fVelocity')
player.speed_steps = config ('player.iSpeedSteps')
player.radius = config ('player.iRadius')

# fps = Data (
# 	font_size=config ('fps.iFontSize'),
# 	alignx=config ('fps.iAlignX'),
# 	aligny=config ('fps.iAlignY')
# )
fps = Data ()
fps.font_size = config ('fps.iFontSize')
fps.alignx = config ('fps.iAlignX')
fps.aligny = config ('fps.iAlignY')

debug = Data ()
debug.mode = config ('debug.iMode')