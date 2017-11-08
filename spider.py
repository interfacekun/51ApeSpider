# -*- coding: utf-8 -*-
##[[
 # @brief:		spider.py

 # @author:		kun si
 # @email:	  	627795061@qq.com
 # @date:		2017-11-07
##]]
import urllib  
import urllib2
import re

class Spider():

	def __init__(self):
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
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

	def getArtistUrl(self, url, reString, headers = None, data = {}, ):
		page = self.GET(url)
		pattern = re.compile(reString)
		return re.finditer(pattern, page)

if __name__ == '__main__':
	spider = Spider()
	url = "http://www.baidu.com/"
	data = {"name":"123", "pwd":"123"}
	page = spider.GET(url, None, data)
	print(page)
	# url = "http://www.51ape.com/artist/"
	# reString = r'<div class="gs_a"><a href="(http://www.51ape.com/\w*/)" class="c47 f_14 b yh">(.*)</a></div>'
	# spider.getArtistUrl(url, reString)