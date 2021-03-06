import time
import math
import os
import random 

def takeAShot(interval, numShots, rand=False):
	""" 
	Function that tells you when to take a shot based on a given interval.
	@param interval: The time interval you want to take a shot in, in minutes
	@param numShots: The number of shots you want to take 
	@param random: randomizes the intervals in which the shots should be taken. The interval will 
		result in a number from 0-10.
	Linux only, I think. If 
	"""	
	for shot in range(numShots):
		flag = False
		start = time.time()
		if (rand == True):
			rand = random.random() * 10
			interval = rand		
		while (flag == False):
			end = time.time()
			if (math.floor(end - start) == 60.0 * interval):
				flag = True
		os.system('say "Time to take a shot"')

