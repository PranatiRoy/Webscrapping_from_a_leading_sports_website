cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
import time
import pandas as pd
from bs4 import BeautifulSoup # for the beautiful soup we have to send the source code for the page.
from selenium import webdriver
browser=webdriver.Chrome(cd)
browser.get("https://www.espncricinfo.com/rankings/content/page/211271.html")
pgsource=browser.page_source # return the source code
soup=BeautifulSoup(pgsource,'html.parser')
head=soup.findAll('h3')

name=[]
for i in head:
	j=i.text
	name.append(j)
#print(name)

import pandas as pd
columns=['pos','team','matches','points','rating']
df=pd.DataFrame(columns=columns)
#print(df)

tr_list=soup.findAll('tr')

n=0
for i in tr_list:
	row=[]
	td_list=i.findAll('td')
	for j in td_list:
		a=j.text
		row.append(a)
		dic={}
	try:
		for k in range(len(df.columns)):
			dic[df.columns[k]] = row[k]
		df = df.append(dic, ignore_index=True)
	except:
		df=pd.DataFrame(columns= columns)
		table_name=name[n]
		n=n+1
	df.to_csv('C:\\Users\\Pranati\\Cricinfo'+table_name+'.csv', index = False)


print("Done")	





