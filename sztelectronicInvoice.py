# -*- coding: utf-8 -*-
import requests
import webbrowser
from selenium import webdriver


date = 20210106
while 1:
	cardnum = input('卡号:')
	webbrowser.open("http://www.shenzhentong.com/ajax/WaterMark.ashx")
	yzm = input('验证码:')

	h={
		"Host": "www.shenzhentong.com",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": "29",
		"Origin": "http://www.shenzhentong.com",
		"Connection": "close",
		"Referer": "http://www.shenzhentong.com/service/invoice_101007009.html",
		"Cookie": "HWWAFSESID=2bb08738a57b3e5324;HWWAFSESTIME=1612775157388;ASP.NET_SessionId=3gczojdfxn2mlpovsex31rzz"
	}
	url = "http://www.shenzhentong.com/Ajax/ElectronicInvoiceAjax.aspx"

	body = {"tp" : "1",
		"yzm" : yzm,
		"cardnum" : cardnum}

	r = requests.post(url,headers=h,data=body)
#	print (r.status_code)
	print (r.text)

	url="http://www.shenzhentong.com/service/fplist_101007009_"+str(cardnum)+"_"+str(date)+".html"

	driver = webdriver.Firefox()
	driver.get("http://www.shenzhentong.com/service/invoice_101007009.html")
	driver.delete_all_cookies()
	cookie1 = {'value': '2bb08738a57b3e5324','name': 'HWWAFSESID'}
	cookie2 = {'value': '1612775157388','name': 'HWWAFSESTIME'}
	cookie3 = {'value': '3gczojdfxn2mlpovsex31rzz','name': 'ASP.NET_SessionId'}
	
	driver.add_cookie(cookie_dict = cookie1)
	driver.add_cookie(cookie_dict = cookie2)
	driver.add_cookie(cookie_dict = cookie3)
	
	driver.get(url)
	driver.find_element_by_name("first_res").click()
	driver.find_element_by_xpath("//div[2]/span").click()
	driver.find_element_by_xpath("(//input[@name='invoice_obj'])[2]").click()
	driver.find_element_by_name("first_res").click()
	driver.find_element_by_id("firmfpmc").click()
	driver.find_element_by_id("firmfpmc").clear()
	driver.find_element_by_id("firmfpmc").send_keys("北京市京都(深圳)律师事务所")
	driver.find_element_by_id("firmsbh").click()
	driver.find_element_by_id("firmsbh").clear()
	driver.find_element_by_id("firmsbh").send_keys("31440000G34802358U")
	driver.find_element_by_id("firmphone").click()
	driver.find_element_by_id("firmphone").clear()
	driver.find_element_by_id("firmphone").send_keys("13312961804")
	driver.find_element_by_name("first_res").click()
	driver.find_element_by_xpath(u"(//input[@value='提交'])[2]").click()
	



