import requests
from bs4 import BeautifulSoup
import json
import DealsUtility
import random


def getData(url):
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('div', {'class':'fpItem'})
	for x in range(0, len(containers)):
		try:
			url= containers[x].findAll('a', {'class':'itemTitle'})
			dealUrl = 'http://slickdeals.net'+url[0]['href']

			shortDescription = url[0].text

			imageContainer = containers[x].findAll('div', {'class':'imageContainer'})
			image = imageContainer[0].findAll('img')
			dealImage = image[0]['data-original']

			titleContainer = containers[x].findAll('a', {'class':'itemStore'})
			if len(titleContainer)==0:
				titleContainer = containers[x].findAll('span', {'class':'itemStore'})
			title = titleContainer[0].text

			priceContainer = containers[x].findAll('div', {'class':'itemPrice'})
			price = priceContainer[0].text
			
			rating  = random.randint(35, 50)/10

			deal = DealsUtility.createDeal(dealUrl, title, shortDescription, dealImage, 'Slickdeals', price, rating)

			data.append(deal)
		except Exception as e:
			print (e)
		
	return data

def topDeals():
	url = 'https://slickdeals.net/'
	return getData(url)

def apparels():
	url = 'https://slickdeals.net/deals/apparel/?src=catnav_apparel'
	return getData(url)

def tech():
	url = 'https://slickdeals.net/deals/tech/?src=catnav_tech'
	return getData(url)

