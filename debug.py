import config as cfg
def log (*args, **kwargs):
	if cfg.debug.mode > 0:
		print (*args, **kwargs)