from bs4 import BeautifulSoup
import requests


def get_url(page):
	product_url = []
	urls = ['http://gz.58.com/pbdn/0/pn{}/'.format(i) for i in range(1, page+1)]
	for url in urls:
		data = requests.get(url)
		soup = BeautifulSoup(data.text, 'lxml')
		product_urls = soup.select('#huishou > tbody > tr.zzinfo > td.t > a')
		for i in product_urls:
			i = 'http://gz.58.com/huishou/' + ((i.get('href').split('info=')[1])[:14]) + 'x.shtml'
			product_url.append(i)
	return product_url


def get_something():
	urls = get_url(1)
	for url in urls:
		ids = (url.split('/')[4].strip('x.shtml'))
		api = 'http://jst1.58.com/counter?infoid={}'.format(ids)
		headers = {
			'Accept': '* / *',
			'Accept-Encoding': 'gzip, deflate, sdch',
			'Accept-Language': 'zh-CN,zh;q=0.8',
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Host': 'jst1.58.com',
			'Referer': 'http://gz.58.com/huishou/{}x.shtml'.format(ids),
			'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
			'Cookie': 'UM_distinctid=160d606e7f6538-0ace1815ddbf07-163a6657-fa000-160d606e7f7773; id58=C6JvElpTdoEFyF2XwRF8aw==; mcity=gz; city=gz; 58home=gz; 58tj_uuid=17212fe5-3a39-48df-b829-71cb7b7a00cc; als=0; commontopbar_myfeet_tooltip=end; xxzl_deviceid=s7kVwMDzBbmi73EQXT9awxMtakj6vjFoUt0bkiwgGvvKorqmaEp1EkgSySaTbf9C; sessionid=77daefa0-b6b1-41dc-8c08-fff5cd2f49da; gr_user_id=ffbfd31e-47bf-42a5-ae83-922e48605aca; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1515421239; wmda_uuid=b2d264065e28d16d7431b5cacd8f7124; wmda_new_uuid=1; wmda_visited_projects=%3B1409632296065; _ga=GA1.2.233523852.1515421240; _gid=GA1.2.851385828.1515421240; new_uv=2; utm_source=; spm=; init_refer=; commontopbar_new_city_info=3%7C%E5%B9%BF%E5%B7%9E%7Cgz; new_session=0; wmda_session_id_1409632296065=1515474679517-3537463c-87f4-5842; gr_session_id_98e5a48d736e5e14=0162c06b-1255-4bd3-bed5-b44a436c1a2b; commontopbar_ipcity=gz%7C%E5%B9%BF%E5%B7%9E%7C0; final_history=21872409023779%2C23909699313845%2C27582306874435%2C23976172639925%2C30105604841905; GA_GTID=0d400067-00a8-5c07-5ef2-7edc7995f012; ppStore_fingerprint=B58C21E66AF1F291A12F838A018DB6A3A57CF11B5A527643%EF%BC%BF1515474688035; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1515475774'
		}
		data = requests.get(api, headers=headers)
		#print(data.text)
		soup = BeautifulSoup(data.text, 'lxml')
		category = soup.select('div.nav > a.crb_a_2')
		if category:
			category = category[0].get_text()
		else:
			category = []
		#title = soup.select('#basicinfo > div.mainTitle > h1')[0].get_text()
		#time = soup.select('#index_show > ul.mtit_con_left.fl > li.time')[0].get_text()
		print(category, data.text)
get_something()
