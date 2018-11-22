import requests
from bs4 import BeautifulSoup
import json
import DealsUtility
import random


def getData(url):
	response = requests.get(url)
	data = json.loads(response.content)

	deals = []

	for i in range(0,len(data['deals'])):
		rating  = random.randint(35, 50)/10
		try:
			deal = DealsUtility.createDeal(data['deals'][i]['dealUrl'], data['deals'][i]['announcementTitle'], data['deals'][i]['highlightsHtml'], data['deals'][i]['largeImageUrl'], 'Groupon', data['deals'][i]['options'][0]['price']['formattedAmount'], rating)
		except Exception as e:
			deal = DealsUtility.createDeal(data['deals'][i]['dealUrl'], data['deals'][i]['announcementTitle'], data['deals'][i]['highlightsHtml'], data['deals'][i]['largeImageUrl'], 'Groupon', 'Deal', rating)
		
		deals.append(deal)
	return deals


def topDeals():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20'
	return getData(url)


def food():
	url='http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:food-and-drink'
	return getData(url)

def menFashion():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:mens-clothing-shoes-and-accessories'
	return getData(url)

def womenFashion():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:womens-clothing-shoes-and-accessories'
	return getData(url)

def electronics():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:electronics'
	return getData(url)

def health():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:health-and-fitness'
	return getData(url)

def home():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:home-improvement'
	return getData(url)

def retail():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:retail'
	return getData(url)

def personalService():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:personal-services'
	return getData(url)

def thingsToDo():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:things-to-do'
	return getData(url)

def toys():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:baby-kids-and-toys'
	return getData(url)

def entertainment():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:entertainment-and-media'
	return getData(url)

def groceries():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:groceries-household-and-pets'
	return getData(url)

def beauty():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:health-and-beauty'
	return getData(url)

def jewelry():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:jewelry-and-watches'
	return getData(url)

def sports():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:sports-and-outdoors'
	return getData(url)

def flights():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:flights-and-transportation'
	return getData(url)

def hotels():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:hotels-and-accommodations'
	return getData(url)

def travel():
	url = 'http://partner-api.groupon.com/deals.json?tsToken=&offset=0&limit=20&filters=category:tour-travel'
	return getData(url)



