#! python3
#downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'  #starting url
os.makedirs('xkcd',exist_ok=True) #store comics in ./xkcd

while not url.endswith('#'):
	

	#1.Download the page.

	print('Downloading page %s...' %url)
	page = requests.get(url)
	page.raise_for_status()

	#2.Find the url of the comic image

	soup = bs4.BeautifulSoup(page.text)

	
	comicElem = soup.select('#comic img')
	if comicElem ==[]:
		print('Could not find the image.')
	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			#3. Download the image.
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:

			#skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com'+prevLink.get('href')
			continue
		

	#4. Save the image to ./xkcd

	imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()




	#5.Get the Prev button's url

	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com'+prevLink.get('href')




print('Done.')