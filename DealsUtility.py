def createDeal(dealUrl, title, shortDescription, dealImage, provider, price, rating):
	deal = {'dealUrl' : '', 'title' : '', 'shortDescription' : '', 'dealImage' : '', 'provider' : 'Groupon', 'price' : '', 'rating' : ''}
	
	deal['dealUrl']=dealUrl
	deal['title']=title
	deal['shortDescription']=shortDescription
	deal['dealImage']=dealImage
	deal['provider']=provider
	deal['price']=price
	deal['rating']=rating

	return deal