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
		self.header = { 'User-Agent' : user_agent }

	def POST(self, url, header = None, data = {}):
		header = header or self.header
		try:
			data = urllib.urlencode(values)
			request = urllib2.Request(url, data, header)
			response = urllib2.urlopen(request, timeout = 10)
			page = response.read()
			return page
		except urllib2.URLError, e:
			print e.reason
			return None

	def GET(self, url, header = None):
		header = header or self.header
		try:
			data = urllib.urlencode(values)
			request = urllib2.Request(url,header = header)
			response = urllib2.urlopen(request, timeout = 10)
			page = response.read()
			return page
		except urllib2.URLError, e:
			print e.reason
			return None



if __name__ == '__main__':