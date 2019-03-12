import threading
import time

# initialize unit variables
SECOND = 'SEC'
MINUTE = 'MIN'
HOUR = 'HOUR'

# Function: run_timer
# Desc: Utilizes a threaded Timer Object
#       Will run passed in function after the timer runs
# Param: valid unit values: SECOND, MINUTE, HOUR
def run_timer( duration, unit, function ):
	
	# calculate duration in seconds
	if( unit == SECOND ):
		seconds = duration
	elif( unit == MINUTE ):
		seconds = duration * 60
	elif( unit == HOUR ):
		seconds = duration * 3600
	else:
		print("Invalid Unit: Defaulting to SECONDS")
		seconds = duration

	# initialize timer object
	timer = threading.Timer( seconds, function)

	# start timer for passed in duration (seconds)
	timer.start()
	# waiting for time completion
	timer.join()

# Function: run_sleep_timer
# Desc: Utilizes time.sleep to run a timer
# Param: valid unit values: SECOND, MINUTE, HOUR
def run_sleep_timer( duration, unit ):
	# calculate duration in seconds
	if( unit == SECOND ):
		seconds = duration
	elif( unit == MINUTE ):
		seconds = duration * 60
	elif( unit == HOUR ):
		seconds = duration * 3600
	else:
		print("Invalid Unit: Defaulting to SECONDS")
		seconds = duration

	# run timer for passed in duration
	time.sleep( seconds )