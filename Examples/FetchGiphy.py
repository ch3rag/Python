import urllib.request
import json

API = 'http://api.giphy.com/v1/gifs/search?&api_key=qumxNc8ObwW96P2aSff907dpJ9Ibu0Pl&limit=1&q='

def getGifUrl(query):
	response = urllib.request.urlopen(API + query)
	data = json.load(response)
	url =  data['data'][0]['images']['fixed_height']['url']
	imageData = urllib.request.urlopen(url).read()
	open("./image.gif", "wb").write(imageData)
	return True

