import requests, bs4
import csv
import pandas as pd


res = requests.get('https://www.gadgetsnow.com/upcoming-mobile-phones')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")


elems = soup.select('.gadget_list')
elems = elems[0]


phone_list = elems.select('.gadget_unit')

title = phone_list[0].select('.gadName')[0].getText()

specs = phone_list[0].select('.specs')
mobile = []

i=0
for i in range(len(phone_list)):
	lst = []
	lst.append(phone_list[i].select('.gadName')[0].getText())
	specs = phone_list[i].select('.specs')
	j=0
	for j in range(len(specs)):
		lst.append(specs[j].select('span')[1].getText())
	mobile.append(lst)

df = pd.DataFrame(mobile,columns=['Title','performance','display','storage','camera'])

df.to_csv('phones.csv',encoding='utf-8',index=False)
