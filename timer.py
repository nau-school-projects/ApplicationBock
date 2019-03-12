import threading
import time

# Function: Timer (utilizes threading library)
def run_timer( minutes, function ):

	# calculate duration in seconds
	seconds = minutes * 60

	# initialize timer object
	timer = threading.Timer( seconds, function)
	
	# start timer for passed in duration (seconds)
	timer.start()

	# waiting for time completion
	timer.join()

# Function: Timer (utilizes time.sleep)
def run_sleep_timer( minutes ):
	
	# calculate duration in seconds
	seconds = minutes * 60

	# run timer for passed in duration
	time.sleep( seconds )


