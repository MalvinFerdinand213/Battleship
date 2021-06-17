import time

class Stopwatch:

	def __init__(self):
		self.start_time = 0
		self.start_stopwatch()


	def time_convert(self, sec):
		mins = sec // 60
		sec = sec % 60
		hours = mins // 60
		mins = mins % 60
		print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

	#input("Press Enter to start")
	#start_time = time.time()

	#input("Press Enter to stop")
	#end_time = time.time()
	def start_stopwatch(self):
		input("Press Enter to start")
		self.start_time = time.time()

	
	def stop_stopwatch(self):
		self.end_time = time.time()
		time_lapsed = self.end_time - self.start_time
		self.time_convert(time_lapsed)