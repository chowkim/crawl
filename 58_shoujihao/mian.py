from time import sleep
from bs4 import BeautifulSoup
import requests
import pymongo


client = pymongo.MongoClient('localhost', 27017)
info = client['info']
page_info = info['page_info']
item_info = info['item_info']


def get_info(page):
	urls = ['http://bj.58.com/jianshenka/pn{}'.format(i) for i in range(page)]
	for url in urls:
		data = requests.get(url)
		sleep(1)
		soup = BeautifulSoup(data.text, 'lxml')
		titles = soup.select('td.t > a')
		title_urls = soup.select('td.t > a')
		for title, link in zip(titles, title_urls):
			data = {
				'link': title.get('href'),
				'title': link.get_text()
			}
			print(data)
			page_info.insert_one(data)


def get_item(urls):
	data = requests.get(urls)
	sleep(1)
	soup = BeautifulSoup(data.text, 'lxml')
	title = soup.select('body > div.w.headline > h1')[0].get_text()
	price = soup.select('body > div > ul > li:nth-of-type(3)')[0].get_text().strip('价格：')
	data = {
		'title': title,
		'price': price
	}
	print(data)
	item_info.insert_one(data)

if __name__ == "__main__":
	get_info(2)
	for info in page_info.find():
		link = info['link']
		get_item(link)
