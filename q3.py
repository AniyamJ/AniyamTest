"""
Importing necessary libraries
"""
from bs4 import BeautifulSoup
import urllib2 
import json


#function to scrape CAVRecord, AppellantName, AppelleeName and DateReceievd for a given page
def scrapeCPI (url):
	#open a url and fetch response
	c = urllib2.urlopen(url)
	chtm = c.read()

	#parse data using beautiful soup
	cpi = BeautifulSoup(chtm, 'html.parser')

	#fetch necessary data using find method provided by soup lib
	output = dict(
			CAVRecordNo = cpi.find("div",{"class":"customtab"}).get_text().replace("CAV Record #","").strip(),
			AppellantName = cpi.find(id="listAllPartiesAPL").tr.td.get_text().strip(),
			AppelleeName = cpi.find(id="listAllPartiesAPE").tr.td.get_text().strip(),
			DateReceived = cpi.find(id="noticeOfAplDt").get("value").strip()
		  	)

	#close the url connection and return output dictionary
	c.close()
	return output


#open a file to write output
outjson = open ("q3.json","w")
#calling function to scrape info and use json.dump write the data into file
json.dump(scrapeCPI("https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry?caseId=23811"), outjson)
#close the file
outjson.close();
