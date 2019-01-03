import requests
from bs4 import BeautifulSoup
import json
import DealsUtility
import random


def getTopDealsData(url):
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('div', {'class':'go-dBox go-smooth'})
	for x in range(0, len(containers)):
		try:
			
			dealUrl = containers[x]['data-dealurl']

			shortDescription = containers[x]['data-dealtitle']

			dealImage = containers[x]['data-imageurl']

			title = containers[x]['data-dmname']

			price = '<b>Rs.' + containers[x]['data-afterprice'] + '</b> <s>Rs.' + containers[x]['data-beforeprice'] +'</s>'

			discountContainer = containers[x].findAll('span', {'class':'go-dodOff'})
			discount = discountContainer[0].text
			
			rating  = discount + '  ' + str(random.randint(35, 50)/10)

			deal = DealsUtility.createDeal(dealUrl, title, shortDescription, dealImage, 'Grabon', price, rating)

			data.append(deal)
		except Exception as e:
			print (e)
		
	return data



def getData(url):
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('div', {'class':'go-coupBox go-smooth go-catCoup'})
	for x in range(0, len(containers)):
		try:

			dealContainer = containers[x].findAll('div', {'class':'go-cTop go-cpn-show'})
			dealContainer2 = dealContainer[0].findAll('div', {'class':'go-cOff'})
			dealContainer3 = dealContainer2[0].findAll('span')
			span = dealContainer3[0].findAll('img')
			# print(1)
			
			dealImage = span[0]['src']
			# print(2)

			strong = dealContainer2[0].findAll('strong')

			# print(3)
			title = strong[0].text
			# print(4)

			dealContainer4 = dealContainer[0].findAll('div', {'class':'go-cTitle'})
			p = dealContainer4[0].findAll('p')
			shortDescription = p[0].text
			# print(5)
		

			dealUrl = 'https://www.grabon.in/coupon-codes/' + containers[x]['data-cid']
			# print(6)

			dealContainer5 = dealContainer4[0].findAll('div', {'class':'go-cBtn'})
			# print(7)
			a = dealContainer5[0].findAll('a')
			small = a[0].findAll('small')


			price = small[0].text

			# print(8)
			
			rating  = str(random.randint(35, 50)/10)

			deal = DealsUtility.createDeal(dealUrl, title, shortDescription, dealImage, 'Grabon', price, rating)

			data.append(deal)
		except Exception as e:
			print (e)
		
	return data




def search(query):
	url = "https://www.grabon.in/search/?q="+query

	print (url)

	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('div', {'class':'go-rcFront go-smooth'})
	for x in range(0, len(containers)):
		try:

			a = containers[x].findAll('a')

			dealUrl = a[0]['href']

			img = a[0].findAll('img')

			dealImage = img[0]['src']
			price = img[0]['alt']

			b = containers[x].findAll('b')

			title = b[0].text

			p = containers[x].findAll('p', {'class':'go-cpn-show'})

			shortDescription = p[0].text
			
			rating  = random.randint(35, 50)/10

			deal = DealsUtility.createDeal(dealUrl, title, shortDescription, dealImage, 'Grabon', price, rating)

			data.append(deal)
		except Exception as e:
			print (e)
		
	return data



def topDeals():
	url = 'https://www.grabon.in/deals/'
	return getTopDealsData(url)

def apparels():
	url = 'https://www.grabon.in/fashion-coupons/'
	return getData(url)


def flight():
	url = 'https://www.grabon.in/flight-coupons/'
	return getData(url)


def home():
	url = 'https://www.grabon.in/home-appliances-coupons/'
	return getData(url)



def recharge():
	url = 'https://www.grabon.in/recharge-coupons/'
	return getData(url)


def travel():
	url = 'https://www.grabon.in/travel-coupons/'
	return getData(url)


def food():
	url = 'https://www.grabon.in/food-coupons/'
	return getData(url)



def footwear():
	url = 'https://www.grabon.in/footwear-coupons/'
	return getData(url)


def electronics():
	url = 'https://www.grabon.in/electronics-coupons/'
	return getData(url)


def retail():
	url = 'https://www.grabon.in/home-and-kitchen-coupons/'
	return getData(url)


def beauty():
	url = 'https://www.grabon.in/beauty-coupons/'
	return getData(url)


def mobile():
	url = 'https://www.grabon.in/mobile-coupons/'
	return getData(url)

def clothes():
	url = 'https://www.grabon.in/clothing-coupons/'
	return getData(url)


def entertainment():
	url = 'https://www.grabon.in/entertainment-coupons/'
	return getData(url)


def flowers():
	url = 'https://www.grabon.in/gifts-and-flowers-coupons/'
	return getData(url)



def gifts():
	url = 'https://www.grabon.in/gifts-and-flowers-coupons/'
	return getData(url)

	
def cameras():
	url = 'https://www.grabon.in/cameras-coupons/'
	return getData(url)

	


def automobile():
	url = 'https://www.grabon.in/automobiles-and-accesssories-coupons/'
	return getData(url)

	

def groceries():
	url = 'https://www.grabon.in/groceries-coupons/'
	return getData(url)



def hotel():
	url = 'https://www.grabon.in/hotel-coupons/'
	return getData(url)


def flight():
	url = 'https://www.grabon.in/flight-coupons/'
	return getData(url)


def baby():
	url = 'https://www.grabon.in/baby-toys-coupons/'
	return getData(url)


def toys():
	url = 'https://www.grabon.in/games-coupons/'
	return getData(url)


def pets():
	url = 'https://www.grabon.in/pets-coupons/'
	return getData(url)

def education():
	url = 'https://www.grabon.in/education-coupons/'
	return getData(url)

def restaurant():
	url = 'https://www.grabon.in/restaurants-coupons/'
	return getData(url)

def health():
	url = 'https://www.grabon.in/health-coupons/'
	return getData(url)

def books():
	url = 'https://www.grabon.in/books-coupons/'
	return getData(url)


def sports():
	url = 'https://www.grabon.in/healthcare-sportsfitness-coupons/'
	return getData(url)

def personal():
	url = 'https://www.grabon.in/beauty-services-coupons/'
	return getData(url)



def events():
	url = 'https://www.grabon.in/event-tickets-coupons/'
	return getData(url)
