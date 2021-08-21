import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(url)
soup=bs[page.text,'html.parser']
pagetable=soup.find_all('table')
temp=[]
tablerows=pagetable[4].find_all('tr')
for tr in tablerows:
	td=tr.find_all('td')
	row=[i.text.rstrip() for i in td]
	temp.append(row)
starname=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp)):
	starname.append(temp[i][0])
	distance.append(temp[i][5])
	mass.append(temp[i][7])
	radius.append(temp[i][8])
df2 = pd.DataFrame(list(zip(starname,distance,mass,radius)),columns=['starname','distance','mass','radius']) 
print(df2) 
df2.to_csv('dwarf_stars.csv')