#generator - a function which yields

#This is a generator which can be called infinte times and takes an initial argument
def daGen(x):

	#an infinite loop 
	while True:
		#increase the value by one
		x = x + 1
		#check the no multiple of 6
		d6 = x % 6
		#check the no multiple of 7
		d7 = x % 7
	
		#if the no multiple of 6 & 7 print "Docket Alarm"
		if(d6 == 0 and 0 == d7): print "Docket Alarm"
		#if the no multiple of 7 print "Docket"
		elif(0 == d7): print "Docket"
		#if the no multiple of 6 print "Alarm"
		elif(0 == d6): print "Alarm"
		#else print no
		else: print x
		
		#yield - where this function stops at this point and will continue when it is invoked by next()
		yield

#one time to call initialize generator
gen = daGen(0)

#loop for 1000 times and call generator using next to complete task
for dA in range(1, 1001): next(gen)
