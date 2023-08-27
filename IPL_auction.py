import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.iplt20.com/auction/2023'
r = requests.get(url)

soup = BeautifulSoup(r.text,'html')

# # Finding Teams in IPL Auction 2023
# teams = soup.find_all('div', class_ = 'agv-team-name')
# for i in teams:
# 	print(i.text)
# # Total number of teams
# print(len(teams))

# # Funds Left
# funds_left = soup.find_all('span','fr-fund')
# for i in range(0,len(funds_left),3):
# 	print(funds_left[i].text) 


table = soup.find('table',class_ = 'ih-td-tab auction-tbl')
title = table.find_all("th")
headers = []
for i in title:
	headers.append(i.get_text())
# print(headers)

df = pd.DataFrame(columns = headers)
# print(df)

rows = table.find_all('tr')
# print(rows)

# As first row is part of table head sp we need to begin from index 1
for i in rows[1:]:
	first_td = i.find_all('td')[0].find("div",class_="ih-pt-ic").text.strip()	
	data = i.find_all('td')[1:]
	row=[tr.text for tr in data] 
	# print(row)
	row.insert(0,first_td)
	l = len(df)
	df.loc[l] = row

print(df)

df.to_csv('IPL_Auction_Stats.csv')