from bs4 import BeautifulSoup
import requests


def get_url(page):
	geturl = []
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		'Cookie': 'abtest_ABTest4SearchDate=b; _ga=GA1.2.1733433819.1515394223; _gid=GA1.2.945018038.1515394223; gr_user_id=c64807b2-67fd-405f-83ec-39c4a08e3872; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=47b49f3e-a74a-4b17-b22a-c9cbb548d2a8; __utma=29082403.1733433819.1515394223.1515394223.1515394223.1; __utmc=29082403; __utmz=29082403.1515394223.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xzuuid=ccd78f09; __utmb=29082403.9.10.1515394223'
	}
	urls = ['http://gz.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1, page+1)]
	for url in urls:
		data = requests.get(url, headers=headers)
		soup = BeautifulSoup(data.text, 'lxml')
		home_urls = soup.select('#page_list > ul > li > a[target="_blank"]')
		for home_url in home_urls:
			home_url = home_url.get('href')
			geturl.append(home_url)
	return geturl


def get_attr():
	urls = get_url(1)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		'Cookie': 'abtest_ABTest4SearchDate=b; _ga=GA1.2.1733433819.1515394223; _gid=GA1.2.945018038.1515394223; gr_user_id=c64807b2-67fd-405f-83ec-39c4a08e3872; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=47b49f3e-a74a-4b17-b22a-c9cbb548d2a8; __utma=29082403.1733433819.1515394223.1515394223.1515394223.1; __utmc=29082403; __utmz=29082403.1515394223.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); xzuuid=ccd78f09; __utmb=29082403.9.10.1515394223'
	}
	for url in urls:
		wb_data = requests.get(url, headers=headers)
		soup = BeautifulSoup(wb_data.text, 'lxml')
		title = soup.select('div.pho_info > h4 > em')[0].get_text()
		address = soup.select('div.pho_info > p')[0].get('title')
		daily_rent = soup.select('#pricePart > div.day_l > span')[0].get_text()
		first_image = soup.select('#curBigImage')[0].get('src')
		landlord_image = soup.select('div.member_pic > a > img')[0].get('src')
		gender = soup.select('div.member_pic > div')[0].get('class')
		if gender == 'member_ico':
			landlord_gender = 'Male'
		else:
			landlord_gender = 'Female'
		landlord_name = soup.select('div.w_240 > h6 > a')[0].get_text()
		data = {
			'title': title,
			'address': address,
			'daily_rent': daily_rent,
			'first_image': first_image,
			'landlord_image': landlord_image,
			'landlord_gender': landlord_gender,
			'landlord_name': landlord_name
		}
		print(data)


if __name__ == "__main__":
	get_attr()
