import requests
import pymongo
from bs4 import BeautifulSoup
from time import sleep


client = pymongo.MongoClient('localhost', 27017)  # create MongoClient
db = client['db']  # create database
sheet_table = db['sheet_table']  # create table


def get_url(page):
	geturl = []
	proxies = {"http": "122.4.42.50:25431"}
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		}
	urls = ['http://gz.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1, page+1)]
	for url in urls:
		sleep(2)
		data = requests.get(url, headers=headers)
		soup = BeautifulSoup(data.text, 'lxml')
		home_urls = soup.select('#page_list > ul > li > a[target="_blank"]')
		for home_url in home_urls:
			home_url = home_url.get('href')
			print(home_url)
			geturl.append(home_url)
	return geturl


def get_attr():
	urls = get_url(1)
	proxies = {"http": "122.4.42.50:25431"}
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		}
	for url in urls:
		sleep(2)
		wb_data = requests.get(url, headers=headers)
		soup = BeautifulSoup(wb_data.text, 'lxml')
		title = soup.select('div.pho_info > h4 > em')[0].get_text()
		address = soup.select('div.pho_info > p')[0].get('title')
		daily_rent = soup.select('#pricePart > div.day_l > span')[0].get_text()
		data = {
			'title': title,
			'address': address,
			'daily_rent': int(daily_rent)
		}
		print(url)
		sheet_table.insert_one(data)


def find_all():
	for item in sheet_table.find():
		if item['daily_rent'] >= 200:
			print(item)

if __name__ == "__main__":
	find_all()
