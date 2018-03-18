#loop from 1 to 1000
for dA in range(1, 1001): 
	#check the no multiple of 6
	d6 = dA % 6
	#check the no multiple of 7
	d7 = dA % 7

	#if the no multiple of 6 & 7 print "Docket Alarm"
	if(d6 ==0 and 0 == d7): print "Docket Alarm"
	#if the no multiple of 7 print "Docket"
	elif(0 == d7): print "Docket"
	#if the no multiple of 6 print "Alarm"
	elif(d6 == 0): print "Alarm"
	#else print no
	else: print dA

# dA = ('Alarm', 'Docket', 'Docket Alarm'); -- Tuples -> values in it can't be changed 
# dA = ['Alarm', 'Docket', 'Docket Alarm']; -- Lists -> values in it can be changed 
