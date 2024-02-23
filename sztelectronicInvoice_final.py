from bs4 import BeautifulSoup
import requests
import webbrowser
import time

date = input('日期:')
while 1:
	cardnum = input('卡号:')
	webbrowser.open("http://www.shenzhentong.com/ajax/WaterMark.ashx")
	yzm = input('验证码:')

	h={
		"Host": "www.shenzhentong.com",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": "29",
		"Origin": "http://www.shenzhentong.com",
		"Connection": "close",
		"Referer": "http://www.shenzhentong.com/service/invoice_101007009.html",
		"Cookie": "HWWAFSESID=403a9735a3e5922d87; HWWAFSESTIME=1623834711714; ASP.NET_SessionId=vgujvcenlj0gdq5sgix3pdht"
	}
	url1 = "http://www.shenzhentong.com/Ajax/ElectronicInvoiceAjax.aspx"

	body1 = {"tp" : "1",
		"yzm" : yzm,
		"cardnum" : cardnum}

	r = requests.post(url1,headers=h,data=body1)


	url2="http://www.shenzhentong.com/service/fplist_101007009_"+str(cardnum)+"_"+str(date)+".html"

	h2={
		'Host': 'www.shenzhentong.com',
		"Cookie": "HWWAFSESID=403a9735a3e5922d87; HWWAFSESTIME=1623834711714; ASP.NET_SessionId=vgujvcenlj0gdq5sgix3pdht",
		'Sec-Ch-Ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
		'Sec-Ch-Ua-Mobile': '?0',
		'Upgrade-Insecure-Requests': '1',
		'Dnt': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Dest': 'document',
		'Referer': 'https://www.shenzhentong.com/service/invoice_101007009.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8',
		'Connection': 'close'
	}

	response = requests.get(url2, headers=h2)
	response.encoding = 'utf-8'
	soup = BeautifulSoup(response.text, features='lxml')

	if str(soup.select('.invoice_info')) == '[<td class="invoice_info"></td>]':
		jlsh = soup.select('.odd_body')[0]['lsh']
		jzdh = soup.select('.odd_body')[0]['zdh']
		jkh = cardnum
		jrq = date
		jsj = soup.select('.odd_body')[0]['sj'] 
		jfirmsbh = '31440000G34802358U'
		jfirmphone ='13342556789'

		h2={
			'Host': 'www.shenzhentong.com',
			"Cookie": "HWWAFSESID=403a9735a3e5922d87; HWWAFSESTIME=1623834711714; ASP.NET_SessionId=vgujvcenlj0gdq5sgix3pdht",
			'Sec-Ch-Ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Dnt': '1',
			'X-Requested-With': 'XMLHttpRequest',
			'Sec-Ch-Ua-Mobile': '?0',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Origin': 'https://www.shenzhentong.com',
			'Sec-Fetch-Site': 'same-origin',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Dest': 'empty',
			'Referer': url2,
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8',
			'Connection': 'close'
		}	

		body2 = {
			"tp" : "3",
			"jlsh" : jlsh,
			"jzdh" : jzdh,
			"jkh" : jkh,
			"jrq" : jrq,
			"jsj" : jsj,
			"jfirmfpmc" : "北京市京都(深圳)律师事务所",
			"jfirmsbh" : "31440000G34802358U",
			"jfirmaddre" : "",
			"jfirmtel" : "",
			"jfirmyh" : "",
			"jfirmyhzh" : "",
			"jfirmphone" : "13342556789"
		}

		r2 = requests.post(url1,headers=h2,data=body2)

		b = r2.text
		pid = b[21:40]
		
		time.sleep(30)
		url3 = 'http://www.shenzhentong.com/service/fpdetail.aspx?nodecode=101007009&pid='+str(pid)
		webbrowser.open(url3)
	else:
		print('已经开过了')
		continue