import requests
import os.path
import pandas as pd

from datetime import datetime
from bs4 import BeautifulSoup

nth = [22,44,66,88,110]
floor = 0
usd = 0
forSales = 0
items = []

page = requests.get("https://www.larvalabs.com/cryptopunks")
soup = BeautifulSoup(page.content, 'html.parser')

def makeCSV(fl,ud,fSal,itms):
	date = datetime.today().strftime('%m/%d/%Y')
	data = [date, fl] + items + [usd, fSal]
	name_dict = {
			'Punk Data':[data[0]], 
			'Floor':[data[1]],
			'Punk 22':[data[2]], 
			'Punk 44':[data[3]],
			'Punk 66':[data[4]],
			'Punk 88':[data[5]],
			'Punk 110':[data[6]],
			'USD':[data[7]],
			'ForSales':[data[8]]
		}

	file_name = 'punks.csv'
	df = pd.DataFrame(name_dict)
	if os.path.exists(file_name):
		df.to_csv(file_name,index=False,mode='a',header=None)
	else:
		df.to_csv(file_name,index=False)

	print (df)



floor_str = soup.findAll(class_='subhead')[0].find('small')

b = floor_str.find('b').getText()
b = b.split()
floor = b[0]
usd = b[2].replace('(','')

a = floor_str.find('a').getText()
a = a.split()
forSales = a[5]



item_str = floor_str.parent.findNext('div').findAll('a')

cnt = len(item_str)
# print(cnt)
for th in nth:
	if th>cnt:
		break
	item = item_str[th-1]['title'].split()
	items.append(item[4])

makeCSV(floor,usd,forSales,items)

