#Importing necessary libraries
import socket

#exception handling - if any exception happens during connect we can print "Not connected"
try:
	#initialize socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#hitting one of the goole's ip to check internet connectivity 
	s.connect(('8.8.4.4', 80)) 
	#if hit is success then fetch local IP that made hit 
	print(s.getsockname()[0]) 
	#close the connection
	s.close() 
except Exception as ex:
	print 'Not connected'
