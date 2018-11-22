from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import json
from flask import Response
from flask_cors import CORS, cross_origin
import groupon
import slickdeals

app = Flask(__name__)
CORS(app)
# url = 'http://localhost/Notifications/'

@app.route('/us/topDeals')
def usTopDeals():
	data = []
	data += groupon.topDeals()
	data += slickdeals.topDeals()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	return Response(json.dumps(response),  mimetype='application/json')

@app.route('/us/fashion')
def usFashion():
	data = []
	data += groupon.menFashion()
	data += groupon.womenFashion()
	data += slickdeals.apparels()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	return Response(json.dumps(response),  mimetype='application/json')

@app.route('/us/electronics')
def usElectronics():
	data = []
	data += groupon.electronics()
	data += slickdeals.tech()
	data.sort(key=lambda x: x['title'])
	response = {'data' : data}
	return Response(json.dumps(response),  mimetype='application/json')
	

@app.route('/notificaionData')
def fetchData():
	url = 'https://www.groupon.com/'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('a')
	for x in range(230, 250):

		url= containers[x]['href']

		image=containers[x].findAll('img', {"data-high-quality":True})
		image=image[0]['data-high-quality']

		title=containers[x].findAll('div', {'class':'cui-udc-subtitle c-txt-gray-dk'})
		if len(title)>0:
			title = str(title[0])[59:-19]
		else:
			title=''

		description=containers[x].findAll('div', {'class':'cui-udc-title-with-subtitle c-txt-black one-line-truncate'})
		if len(description)>0:
			description=str(description[0])[84:-17]
		else:
			description=''
		OneNotification={'image':image, 'title':title, 'description':description, 'url':url}
		data.append(OneNotification)

	return Response(json.dumps(data),  mimetype='application/json')




@app.route('/notificaionData2')
def notificaionData2():
	url = 'https://www.groupon.com/'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('a')
	for x in range(218, 245):

		url= containers[x]['href']

		image=containers[x].findAll('img', {"data-high-quality":True})
		image=image[0]['data-high-quality']

		title=containers[x].findAll('div', {'class':'cui-udc-subtitle c-txt-gray-dk'})
		if len(title)>0:
			title = str(title[0])[59:-19]
		else:
			title=''

		description=containers[x].findAll('div', {'class':'cui-udc-title-with-subtitle c-txt-black one-line-truncate'})
		if len(description)>0:
			description=str(description[0])[84:-17]
		else:
			description=''
		OneNotification={'image':image, 'title':title, 'description':description, 'url':url}
		data.append(OneNotification)

	return Response(json.dumps(data),  mimetype='application/json')





@app.route('/grouponHome')
def grouponHome():
	url = 'https://www.groupon.com/'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('a')
	for x in range(208, 219):

		# print containers[x]['href']
		url= containers[x]['href']

		image=containers[x].findAll('img', {"data-high-quality":True})
		# print x
		# print image
		image=image[0]['data-high-quality']

		title=containers[x].findAll('div', {'class':'cui-udc-subtitle c-txt-gray-dk'})
		if len(title)>0:
			# # print str(title[0])[59:-19]
			title = str(title[0])[59:-19]
		else:
			title=''

		description=containers[x].findAll('div', {'class':'cui-udc-title-with-subtitle c-txt-black one-line-truncate'})
		if len(description)>0:
			# print str(description[0])[84:-17]
			description=str(description[0])[84:-17]
		else:
			description=''
		OneNotification={'image':image, 'title':title, 'description':description, 'url':url}
		data.append(OneNotification)


	return Response(json.dumps(data),  mimetype='application/json')




@app.route('/grouponRestaurant')
def grouponRestaurant():
	url = 'https://www.groupon.com/occasion/groupon-plus'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('a')
	for x in range(218, 260):

		# print containers[x]['href']
		url= containers[x]['href']

		image=containers[x].findAll('img', {"data-high-quality":True})
		# print x
		# print image
		image=image[0]['data-high-quality']

		title=containers[x].findAll('div', {'class':'cui-udc-subtitle c-txt-gray-dk'})
		if len(title)>0:
			# # print str(title[0])[59:-19]
			title = str(title[0])[59:-19]
		else:
			title=''

		description=containers[x].findAll('div', {'class':'cui-udc-title-with-subtitle c-txt-black one-line-truncate'})
		if len(description)>0:
			# print str(description[0])[84:-17]
			description=str(description[0])[84:-17]
		else:
			description=''
		OneNotification={'image':image, 'title':title, 'description':description, 'url':url}
		data.append(OneNotification)


	return Response(json.dumps(data),  mimetype='application/json')






@app.route('/grouponGoods')
def grouponGoods():
	url = 'https://www.groupon.com/goods'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('a')
	for x in range(213, 245):

		# print containers[x]['href']
		url= containers[x]['href']

		image=containers[x].findAll('img', {"data-high-quality":True})
		# print x
		# print image
		image=image[0]['data-high-quality']

		title=containers[x].findAll('div', {'class':'cui-udc-subtitle c-txt-gray-dk'})
		if len(title)>0:
			# print str(title[0])[59:-19]
			title = str(title[0])[59:-19]
		else:
			title=''

		description=containers[x].findAll('div', {'class':'cui-udc-title-with-subtitle c-txt-black one-line-truncate'})
		if len(description)>0:
			# print str(description[0])[84:-17]
			description=str(description[0])[84:-17]
		else:
			description=''
		OneNotification={'image':image, 'title':title, 'description':description, 'url':url}
		data.append(OneNotification)


	return Response(json.dumps(data),  mimetype='application/json')









@app.route('/grabonMostUsed')
def grabonMostUsed():
	url = 'http://www.grabon.in/twentyfour/gettabdata?tabId=1'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		# print containers[x]
		# url= containers[x]['href']
		try:
			image=containers[x].findAll('img')
			# print x
			# print image
			image=image[0]['src']
			# print image

			title=containers[x].findAll('div', {'class':'sc-h3'})
			title=title[0].text
			# print title

			description=containers[x].findAll('h3', {'class':'sc-h4'})
			description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 's-code'})
			couponCode=couponCode[0].text


			OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

		


	return Response(json.dumps(data),  mimetype='application/json')





@app.route('/grabonRecharge')
def grabonRecharge():
	url = 'http://www.grabon.in/twentyfour/gettabdata?tabId=6'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		# print containers[x]
		# url= containers[x]['href']
		try:
			image=containers[x].findAll('img')
			# print x
			# print image
			image=image[0]['src']
			# print image

			title=containers[x].findAll('div', {'class':'sc-h3'})
			title=title[0].text
			# print title

			description=containers[x].findAll('h3', {'class':'sc-h4'})
			description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 's-code'})
			couponCode=couponCode[0].text

			if len(couponCode)<=3:
				couponCode="No Coupon Code Required"


			OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

		


	return Response(json.dumps(data),  mimetype='application/json')





@app.route('/grabonTravel')
def grabonTravel():
	url = 'http://www.grabon.in/twentyfour/gettabdata?tabId=5'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		# print containers[x]
		# url= containers[x]['href']
		try:
			image=containers[x].findAll('img')
			# print x
			# print image
			image=image[0]['src']
			# print image

			title=containers[x].findAll('div', {'class':'sc-h3'})
			title=title[0].text
			# print title

			description=containers[x].findAll('h3', {'class':'sc-h4'})
			description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 's-code'})
			couponCode=couponCode[0].text

			if len(couponCode)<=3:
				couponCode="No Coupon Code Required"


			OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

		


	return Response(json.dumps(data),  mimetype='application/json')









@app.route('/grabonFashion')
def grabonFashion():
	url = 'http://www.grabon.in/twentyfour/gettabdata?tabId=7'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		# print containers[x]
		# url= containers[x]['href']
		try:
			image=containers[x].findAll('img')
			# print x
			# print image
			image=image[0]['src']
			# print image

			title=containers[x].findAll('div', {'class':'sc-h3'})
			title=title[0].text
			# print title

			description=containers[x].findAll('h3', {'class':'sc-h4'})
			description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 's-code'})
			couponCode=couponCode[0].text

			if len(couponCode)<=3:
				couponCode="No Coupon Code Required"


			OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

		


	return Response(json.dumps(data),  mimetype='application/json')









@app.route('/grabonFood')
def grabonFood():
	url = 'http://www.grabon.in/twentyfour/gettabdata?tabId=4'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		# print containers[x]
		# url= containers[x]['href']
		try:
			image=containers[x].findAll('img')
			# print x
			# print image
			image=image[0]['src']
			# print image

			title=containers[x].findAll('div', {'class':'sc-h3'})
			title=title[0].text
			# print title

			description=containers[x].findAll('h3', {'class':'sc-h4'})
			description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 's-code'})
			couponCode=couponCode[0].text

			if len(couponCode)<=3:
				couponCode="No Coupon Code Required"


			OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

		


	return Response(json.dumps(data),  mimetype='application/json')









@app.route('/grabonElectronics')
def grabonElectronics():
	url = 'http://www.grabon.in/twentyfour/gettabdata?tabId=2'
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		# print containers[x]
		# url= containers[x]['href']
		try:
			image=containers[x].findAll('img')
			# print x
			# print image
			image=image[0]['src']
			# print image

			title=containers[x].findAll('div', {'class':'sc-h3'})
			title=title[0].text
			# print title

			description=containers[x].findAll('h3', {'class':'sc-h4'})
			description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 's-code'})
			couponCode=couponCode[0].text

			if len(couponCode)<=3:
				couponCode="No Coupon Code Required"


			OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

		


	return Response(json.dumps(data),  mimetype='application/json')







@app.route('/grabonSearch/<query>')
def grabonSearch(query):
	# print query
	url = 'http://www.grabon.in/search/?q='+query
	response = requests.get(url)
	html = response.content

	data=[]
	
	soup = BeautifulSoup(html, "html.parser")

	# containers=soup.findAll('div', {'class':'cui-content c-bdr-gray-clr ch-bdr-gray-md'})
	containers=soup.findAll('article')
	for x in range(0, len(containers)):

		print (containers[x])
		# url= containers[x]['href']
		try:
			# image=containers[x].findAll('img')
			# print x
			# print image
			# image=image[0]['data-original']
			# print (image)

			# title=containers[x].findAll('div', {'class':'sc-h3'})
			# title=title[0].text
			# print title


			title=containers[x].findAll('h3', {'class':'go-cpn-show'})
			title=title[0].text

			# description=containers[x].findAll('h3', {'class':'sc-h4'})
			# description=description[0].text
			# print description
			
			# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
			# # longDescription=longDescription[0]


			couponCode=containers[x].findAll('div', {'class': 'go-cpBtn'})
			# couponCode=couponCode[0].text
			couponCode=couponCode[0].findAll('span')[0].text

			if len(couponCode)<=3:
				couponCode="No Coupon Code Required"


			# OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
			OneNotification={'title':title,  'couponCode':couponCode}
			data.append(OneNotification)

		except:
			pass

	if len(data)==0:
		containers=soup.findAll('article', {'class' : 'sm-coupon'})
		for x in range(0, len(containers)):

			# print containers[x]
			# url= containers[x]['href']
			try:
				
				image=''
				# print image

				
				title=''
				# # print title

				description=containers[x].findAll('h3', {'class':'smci-h'})
				description=description[0].text
				# print description
				
				# longDescription=containers[x].findAll('div', {'class':'sc-des go-desc about-merchant'})
				# # longDescription=longDescription[0]


				couponCode=containers[x].findAll('div', {'class': 'sm-code'})
				couponCode=couponCode[0].text

				if len(couponCode)<=3:
					couponCode="No Coupon Code Required"


				OneNotification={'image':image, 'title':title, 'description':description, 'couponCode':couponCode}
				data.append(OneNotification)

			except:
				pass
		

		


	return Response(json.dumps(data),  mimetype='application/json')






if __name__ == '__main__':
    app.run()