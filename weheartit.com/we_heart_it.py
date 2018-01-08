from bs4 import BeautifulSoup
import requests
import urllib.request
import os


def get_img_url(page):
	images = []
	urls = ['https://weheartit.com/inspirations/taylorswift?page={}&before=6106024'.format(i) for i in range(1, page+1)]
	for url in urls:
		image_data = requests.get(url)
		soup = BeautifulSoup(image_data.text, 'lxml')
		img_urls = soup.select('a.js-entry-detail-link > img')
		for img_url in img_urls:
			img = img_url.get('src')
			images.append(img)
	return images


def create_folder(path):
	is_exists = os.path.exists(path)
	if not is_exists:
		print('[*]新建文件夹', path)
		os.makedirs(path)
	else:
		print('[+]文件夹', path, '已创建')


def download_image():
	img_urls = get_img_url(1)
	path = '/Users/job/PycharmProjects/crawl_for_four_week/weheartit.com/images/'
	create_folder(path)
	for img_url in img_urls:
		filename = path + img_url.split('/')[-2] + img_url.split('/')[-1]
		print(filename)
		urllib.request.urlretrieve(img_url, filename)

if __name__ == "__main__":
	download_image()
	# asd = get_img_url(1)
	# for i in asd:
	# 	print(i.split('/')[-1])
