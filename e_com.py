import requests
from bs4 import BeautifulSoup


url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)
# print(r)

soup = 	BeautifulSoup(r.text, 'html')
# print(soup)

boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')
print('Total no. of boxes:',len(boxes))


# Finding Names of all Tablets
names = soup.find_all('a', class_ = 'title')
# print(names)
for i in names:
	print(i.text)

# Finding Price of Tablets
price = soup.find_all('h4', class_= 'pull-right price')
for i in price:
	print(i.text)

# Finding reviews
reviews = soup.find_all('p', class_ = 'pull-right')
for i in reviews:
	print(i.text)