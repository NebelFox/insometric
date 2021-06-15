# import atexit
from time import time
start_time = time ()
next_name = 0
print ("Starting time: {}".format (start_time))

def timepoint (name=None):
	global start_time, next_name
	endtime = time ()
	delta = (endtime - start_time) * 1000
	if not name:
		name = next_name
		next_name += 1
	print ("Timepoint: {}; Elapsed time: {} ms".format (name, delta))
	start_time = endtime
	return endtime, delta

# atexit.register (onexit)