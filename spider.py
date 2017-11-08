# -*- coding: utf-8 -*-
##[[
 # @brief:		spider.py

 # @author:		kun si
 # @email:	  	627795061@qq.com
 # @date:		2017-11-07
##]]
import urllib  
import urllib2

class Spider():

	def __init__(self):
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = {'User-Agent':self.user_agent}

	def POST(self, url, headers = None, data = {}):
		headers = headers or self.headers
		try:

			if data :
				data = urllib.urlencode(data)

			request = urllib2.Request(url, data, headers)
			response = urllib2.urlopen(request, timeout = 10)
			page = response.read()
			return page
		except urllib2.URLError, e:
			print e.reason
			return None

	def GET(self, url, headers = None, data = {}):
		headers = headers or self.headers
		try:

			if data :
				dataStr = urllib.urlencode(data)
				url = url + "?" + dataStr
				print(url)

			request = urllib2.Request(url,headers = headers)
			response = urllib2.urlopen(request, timeout = 10)
			page = response.read()
			return page
		except urllib2.URLError, e:
			print e.reason
			return None

if __name__ == '__main__':
	spider = Spider()
	url = "http://www.baidu.com/"
	data = {"name":"123", "pwd":"123"}
	page = spider.GET(url, None, data)
	print(page)