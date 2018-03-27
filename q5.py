#Importing necessary libraries

from bs4 import BeautifulSoup
import requests 

"""
***Then have the program click the checkbox, and select continue, download the resulting case
search page and save it into a file named q5-2.html***

The above simulation can be done via librairies like selenium. 
I've done a Workaround here using post request.  
Reason for using requests lib is truncation of html response while using urllib

"""

#function to download page
def downloadPage (url, filename, params):

	#checking for parmas whether to make post or get request for this use case
	if not params:
		cs = requests.get(url)
	else:
		cs = requests.post(url,data=params) #no need of encoding the params here

	#open a file to write output
	q5 = open (filename,"w")
	#fomrat the output and write in utf-8 format		
	q5.write(BeautifulSoup(cs.text, 'html.parser').prettify().encode('utf-8'))
	#close output file
	q5.close()

	#close url connection
	cs.close();


#calling functions to do actual task
downloadPage("http://casesearch.courts.state.md.us/casesearch/","q5-1.html", None)
downloadPage("http://casesearch.courts.state.md.us/casesearch/processDisclaimer.jis","q5-2.html",{"disclaimer":"Y"})
