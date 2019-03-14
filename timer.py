import time

# Function: run_sleep_timer
# Desc: Utilizes time.sleep to run a timer
def runTimer( hours, minutes ):

	# initalizing variables
	hours = hours
	minutes = minutes;
	seconds = 0

	# calculate total duration in seconds
	duration = int(( hours * 3600 ) + ( minutes * 60 ))

	# iterate through duration ( 0 to duration )
	for i in range(duration):
		if seconds == 0:
			if minutes != 0:
				minutes = minutes - 1
				seconds = 60
		if minutes == 0:
			if hours != 0:
				hours = hours - 1
				minutes = 59
				seconds = 60

		# decremenet seconds
		seconds = seconds - 1

		# wait for 1 second
		time.sleep(1)

		# output current timer countdown
		print( hours, ":", minutes, ":", seconds )