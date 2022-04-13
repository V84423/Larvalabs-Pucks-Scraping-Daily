import requests
import os.path
import pandas as pd

from datetime import datetime
from bs4 import BeautifulSoup

nth = [22,44,66,88,110,132,154,176,198,220,242,264,286,308,330,352]

page = requests.get("https://larvalabs.com/cryptopunks/forsale")
soup = BeautifulSoup(page.content, 'html.parser')
items_str = soup.findAll(class_='punk-image-container-dense')
print("Total Items: ", len(items_str))
def makeCSV():
	date = datetime.today().strftime('%m/%d/%Y')	
	name_dict = dict({'Date':[date]})

	for th in nth:
		item = items_str[th-1].find('a')['title'].split()
		name_dict.update({'Punk '+str(th): [item[4]]})

	file_name = 'punk_items.csv'
	df = pd.DataFrame(name_dict)
	if os.path.exists(file_name):
		df.to_csv(file_name,index=False,mode='a',header=None)
	else:
		df.to_csv(file_name,index=False)

	print (df)

makeCSV()

