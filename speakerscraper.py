from selenium import webdriver
import time
import pdb
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ITC2017Summary.settings")
django.setup()
from contentsummary.models import Speaker, Company
#pdb.set_trace()

start_time = time.mktime(time.localtime())
print("{}: Starting pull".format(time.strftime('%H:%M',time.localtime())))
options = webdriver.ChromeOptions()
options.binary_location = 'C:\Program Files (x86)\Google\Chrome Dev\Application\chrome.exe'
#The headless option below will make it so that the chrome window does not visibly appear
#options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = options)
driver.implicitly_wait(15)

#go to the  website
driver.get('http://insuretechconnect.com/speakers/')

#Get the html and process it
processedhtml = BeautifulSoup(driver.page_source,'html.parser')
rows = processedhtml.find_all(class_='edgtf-team-inner')

#Create the list which will have all of the results
speakers = []
companies = []

#loop through each row to create the dictionary
for row in rows:
	individualresult = {}

	
	#Pull the data elements
	individualresult['Name'] = row.find(class_='edgtf-team-name').get_text().strip()
	if individualresult['Name'] == "TED NICKEL":
		titleandcompany=['COMMISSIONER OF INSURANCE','THE STATE OF WISCONSIN']
	else:
		titleandcompany = row.find(class_='edgtf-team-position').get_text().split('@')
	individualresult['Title'] = titleandcompany[0].strip()
	individualresult['Company'] = titleandcompany[1].strip()
	individualresult['Details'] = row.find(class_='speaker-details').get_text().strip()

	companies.append(titleandcompany[1].strip())
	speakers.append(individualresult)

	#Saves the image
	#urllib.request.urlretrieve(row.find(class_='edgtf-team-image').find(src=True)['src'],'Scraped Photos/{}.jpg'.format(individualresult['Name']))

#Creates a dataframe from the results, with the name as the key
speakers_df = pd.DataFrame(speakers)
speakers_df = speakers_df.set_index('Name')

#Pulls the unique values of the companies
companies = set(companies)
companies_df = pd.DataFrame(list(companies))

#Adds the items to Django
for company in companies:
	newcompany = Company()
	newcompany.name = company
	newcompany.save()

for speaker in speakers:
	newspeaker = Speaker()
	newspeaker.name = speaker['Name']
	newspeaker.details = speaker['Details']
	newspeaker.title = speaker['Title']
	newspeaker.company = Company.objects.get(name=speaker['Company'])
	newspeaker.save()
	
#closes the window
driver.close()
end_time = time.mktime(time.localtime())
print("{}: Scrape complete! Runtime was {:.0f} minutes".format(time.strftime('%H:%M',time.localtime()),(end_time-start_time)/60))