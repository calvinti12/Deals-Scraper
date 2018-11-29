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
	url = 'https://slickdeals.net/deals/apparel/'
	return getData(url)

def tech():
	url = 'https://slickdeals.net/deals/tech/'
	return getData(url)

def restaurant():
	url = 'https://slickdeals.net/deals/restaurant/'
	return getData(url)


def shoes():
	url = 'https://slickdeals.net/deals/shoes/'
	return getData(url)

def phone():
	url = 'https://slickdeals.net/deals/phone/'
	return getData(url)

def tv():
	url = 'https://slickdeals.net/tv-deals/'
	return getData(url)

def apple():
	url = 'https://slickdeals.net/deals/apple/'
	return getData(url)

def auto():
	url = 'https://slickdeals.net/deals/auto/'
	return getData(url)

def books():
	url = 'https://slickdeals.net/deals/books-magazines/'
	return getData(url)


def children():
	url = 'https://slickdeals.net/deals/children/'
	return getData(url)

def computer():
	url = 'https://slickdeals.net/computer-deals/'
	return getData(url)

def education():
	url = 'https://slickdeals.net/deals/education/'
	return getData(url)



def entertainment():
	url = 'https://slickdeals.net/deals/entertainment/'
	return getData(url)

def flowers():
	url = 'https://slickdeals.net/deals/flowers-gifts/'
	return getData(url)

def grocery():
	url = 'https://slickdeals.net/deals/grocery/'
	return getData(url)



def beauty():
	url = 'https://slickdeals.net/deals/beauty/'
	return getData(url)

def home():
	url = 'https://slickdeals.net/deals/home/'
	return getData(url)

def movie():
	url = 'https://slickdeals.net/deals/movie/'
	return getData(url)


def seasonal():
	url = 'https://slickdeals.net/deals/seasonal/'
	return getData(url)

def pets():
	url = 'https://slickdeals.net/deals/pets/'
	return getData(url)

def sport():
	url = 'https://slickdeals.net/deals/sport/'
	return getData(url)

	
def travel():
	url = 'https://slickdeals.net/travel-deals/'
	return getData(url)


def game():
	url = 'https://slickdeals.net/video-game-deals/'
	return getData(url)

	
def personal():
	url = 'https://slickdeals.net/deals/personal-care/'
	return getData(url)

