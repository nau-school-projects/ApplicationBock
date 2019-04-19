import unittest
from CantTouchThisInterface import *

# setting up the testing class
class TimerTestCase( unittest.TestCase ):

	# initialization
	def setUp( self ):
		self.startTime = "10:58"
		self.stopTime = "10:59"
		self.hoursDur = "0"
		self.minutesMin = "1"

	# test block scheduling
	def testScheduler( self ):
		test = CantTouchThisInterface.scheduleTimer( self )
		self.assertTrue( test, 1 )

# run all tests
if __name__ == "__main__":
	unittest.main()	