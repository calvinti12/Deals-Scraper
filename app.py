from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import json
from flask import Response
from flask_cors import CORS, cross_origin
import groupon
import slickdeals
import grabon
from github import Github

app = Flask(__name__)
CORS(app)
# url = 'http://localhost/Notifications/'

g = Github("anupkumarpanwar", "Sdtbtwtbtitbtewbsap@1511")
repo = g.get_repo("anupkumarpanwar/dealsserver")

@app.route('/us/fetchData')
def usFetchData():

	# US Top Deals
	data = []
	data += groupon.topDeals()
	data += slickdeals.topDeals()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usTopDeals.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usTopDeals.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usTopDeals.json", "updated data", json.dumps(response), branch="master")

	# US Fashion
	data = []
	data += groupon.menFashion()
	data += groupon.womenFashion()
	data += slickdeals.apparels()
	data += slickdeals.shoes()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usClothes.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usClothes.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usClothes.json", "updated data", json.dumps(response), branch="master")

	# US Electronics
	data = []
	data += groupon.electronics()
	data += slickdeals.tech()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usElectronics.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usElectronics.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usElectronics.json", "updated data", json.dumps(response), branch="master")



	# US Food
	data = []
	data += groupon.food()
	data += slickdeals.restaurant()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usFood.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usFood.json", "updated data", json.dumps(response), branch="master")



	# US Lifestyle
	data = []
	data += groupon.health()
	data += groupon.jewelry()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usLifestyle.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usLifestyle.json", "updated data", json.dumps(response), branch="master")


	# US Entertainment
	data = []
	data += slickdeals.entertainment()
	data += groupon.entertainment()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usEntertainment.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usEntertainment.json", "updated data", json.dumps(response), branch="master")




	# US Home Appliances
	data = []
	data += slickdeals.home()
	data += groupon.home()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usHome Appliances.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usHome Appliances.json", "updated data", json.dumps(response), branch="master")




	# US Retail
	data = []
	data += groupon.retail()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usRetail.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usRetail.json", "updated data", json.dumps(response), branch="master")



	
	# US Personal Services
	data = []
	data += groupon.personalService()
	data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usPersonal Services.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usPersonal Services.json", "updated data", json.dumps(response), branch="master")


	
	# US Things To Do
	data = []
	data += groupon.thingsToDo()
	data += slickdeals.seasonal()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usThings To Do.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usThings To Do.json", "updated data", json.dumps(response), branch="master")



	
	# US Toys
	data = []
	data += groupon.toys()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usToys.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usToys.json", "updated data", json.dumps(response), branch="master")




	
	# US Groceries
	data = []
	data += groupon.groceries()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usGroceries.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usGroceries.json", "updated data", json.dumps(response), branch="master")



	
	# US Beauty
	data = []
	data += groupon.beauty()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usBeauty.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usBeauty.json", "updated data", json.dumps(response), branch="master")



	
	# US Accessories
	data = []
	data += slickdeals.phone()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usAccessories.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usAccessories.json", "updated data", json.dumps(response), branch="master")



	
	# US Sports
	data = []
	data += groupon.sports()
	data += slickdeals.sport()
	data += slickdeals.game()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usSports.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usSports.json", "updated data", json.dumps(response), branch="master")



	# US Travel
	data = []
	data += groupon.travel()
	data += groupon.flights()
	data += slickdeals.travel()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usTravel.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usTravel.json", "updated data", json.dumps(response), branch="master")



	# US Hotels
	data = []
	data += groupon.hotels()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usHotels.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usHotels.json", "updated data", json.dumps(response), branch="master")



	# US Pets
	data = []
	data += slickdeals.pets()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usPets.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usPets.json", "updated data", json.dumps(response), branch="master")





	# US Books
	data = []
	data += slickdeals.education()
	data += slickdeals.books()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usBooks.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usBooks.json", "updated data", json.dumps(response), branch="master")




	# US Flowers
	data = []
	data += slickdeals.flowers()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usFlowers.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usFlowers.json", "updated data", json.dumps(response), branch="master")



	# US Automotive
	data = []
	data += slickdeals.auto()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usAutomotive.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usAutomotive.json", "updated data", json.dumps(response), branch="master")




	# US Photography
	data = []
	data += slickdeals.movie()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usPhotography.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usPhotography.json", "updated data", json.dumps(response), branch="master")




	# US Baby
	data = []
	data += slickdeals.children()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usBaby.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usBaby.json", "updated data", json.dumps(response), branch="master")




	# US Gifts
	data = []
	data += slickdeals.gift()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/usFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/usGifts.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/usGifts.json", "updated data", json.dumps(response), branch="master")


	return Response('Data fetched successfully.')




@app.route('/us/search/<query>')
def usSearch(query):
	data = []
	data += slickdeals.search(query)
	response = {'data' : data}
	return Response(json.dumps(response),  mimetype='application/json')







@app.route('/india/fetchData')
def indiaFetchData():

	# india Top Deals
	data = []
	data += grabon.topDeals()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaTopDeals.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaTopDeals.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaTopDeals.json", "updated data", json.dumps(response), branch="master")

	# india Fashion
	data = []
	data += grabon.apparels()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaClothes.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaClothes.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaClothes.json", "updated data", json.dumps(response), branch="master")

	# india Electronics
	data = []
	data += grabon.electronics()
	data += grabon.mobile()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaElectronics.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaElectronics.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaElectronics.json", "updated data", json.dumps(response), branch="master")



	# india Food
	data = []
	data += grabon.food()
	data += grabon.restaurant()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaFood.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaFood.json", "updated data", json.dumps(response), branch="master")



	# india Lifestyle
	data = []
	data += grabon.health()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaLifestyle.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaLifestyle.json", "updated data", json.dumps(response), branch="master")


	# india Entertainment
	data = []
	data += grabon.entertainment()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaEntertainment.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaEntertainment.json", "updated data", json.dumps(response), branch="master")




	# india Home Appliances
	data = []
	data += grabon.home()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaHome Appliances.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaHome Appliances.json", "updated data", json.dumps(response), branch="master")




	# india Retail
	data = []
	data += grabon.retail()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaRetail.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaRetail.json", "updated data", json.dumps(response), branch="master")



	
	# india Personal Services
	data = []
	data += grabon.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaPersonal Services.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaPersonal Services.json", "updated data", json.dumps(response), branch="master")


	
	# india Things To Do
	data = []
	data += grabon.events()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaThings To Do.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaThings To Do.json", "updated data", json.dumps(response), branch="master")



	
	# india Toys
	data = []
	data += grabon.toys()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaToys.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaToys.json", "updated data", json.dumps(response), branch="master")




	
	# india Groceries
	data = []
	data += grabon.groceries()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaGroceries.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaGroceries.json", "updated data", json.dumps(response), branch="master")



	
	# india Beauty
	data = []
	data += grabon.beauty()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaBeauty.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaBeauty.json", "updated data", json.dumps(response), branch="master")



	
	# india Accessories
	data = []
	data += grabon.mobile()
	data += grabon.recharge()
	# data += slickdeals.personal()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaAccessories.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaAccessories.json", "updated data", json.dumps(response), branch="master")



	
	# india Sports
	data = []
	data += grabon.sports()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaSports.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaSports.json", "updated data", json.dumps(response), branch="master")



	# india Travel
	data = []
	data += grabon.travel()
	data += grabon.flight()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaTravel.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaTravel.json", "updated data", json.dumps(response), branch="master")



	# india Hotels
	data = []
	data += grabon.hotel()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaHotels.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaHotels.json", "updated data", json.dumps(response), branch="master")



	# india Pets
	data = []
	data += grabon.pets()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaPets.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaPets.json", "updated data", json.dumps(response), branch="master")

	return Response('Data fetched successfully.')



@app.route('/india/fetchData2')
def indiaFetchData2():

	# india Books
	data = []
	data += grabon.education()
	data += grabon.books()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaBooks.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaBooks.json", "updated data", json.dumps(response), branch="master")




	# india Flowers
	data = []
	data += grabon.flowers()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaFlowers.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaFlowers.json", "updated data", json.dumps(response), branch="master")



	# india Automotive
	data = []
	data += grabon.automobile()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaAutomotive.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaAutomotive.json", "updated data", json.dumps(response), branch="master")




	# india Photography
	data = []
	data += grabon.cameras()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaPhotography.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaPhotography.json", "updated data", json.dumps(response), branch="master")




	# india Baby
	data = []
	data += grabon.baby()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaBaby.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaBaby.json", "updated data", json.dumps(response), branch="master")




	# india Gifts
	data = []
	data += grabon.gifts()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	# output_file = open('./coupons_data/indiaFood.json','w+')
	# json.dump(response, output_file)
	try:
		contents = repo.get_contents("coupons_data/indiaGifts.json", ref="master")
		repo.delete_file(contents.path, "removed data", contents.sha, branch="master")
	except:
		pass
	repo.create_file("coupons_data/indiaGifts.json", "updated data", json.dumps(response), branch="master")


	return Response('Data fetched successfully.')




@app.route('/india/search/<query>')
def indiaSearch(query):
	data = []
	data += slickdeals.search(query)
	response = {'data' : data}
	return Response(json.dumps(response),  mimetype='application/json')












if __name__ == '__main__':
    app.run()