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
import time
import chardet
from dao import Dao

class Spider():

	def __init__(self):
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		self.headers = {'User-Agent':self.user_agent}
		self.dao = Dao()
		self.dao.connect()

	def POST(self, url, headers = None, data = {}):
		headers = headers or self.headers
		try:

			if data :
				data = urllib.urlencode(data)

			request = urllib2.Request(url, data, headers)
			response = urllib2.urlopen(request, timeout = 30)
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
			response = urllib2.urlopen(request, timeout = 30)
			page = response.read()
			return page
		except urllib2.URLError, e:
			print e.reason
			return None

	def spiderUrl(self, url, reString, headers = None, data = {}):
		page = self.GET(url)
		pattern = re.compile(reString)
		return re.finditer(pattern, page)

	def spiderPage(self, page, reString):
		pattern = re.compile(reString)
		return re.finditer(pattern, page)

	def getArtistMuisc(self, url, artist, headers = None, data = {}):
		page = self.GET(url)
		if isinstance(artist, unicode) :
			artist = artist.encode('utf-8')
		reString = r'<a href="/.*/index_(\d*).html">尾页</a>'
		if type(page) == type('a') :
			results = re.search(re.compile(reString, re.S), page)
			if results :
					maxPage = int(results.group(1))
					print("maxPage %d" % (maxPage))
					for i in range(1, maxPage+1) :
						tempUrl = url
						if i != 1 :
							tempUrl = url + 'index_' + str(i) + '.html'
						print("spider url: %s" % (tempUrl))
						page = self.GET(tempUrl)
						reString = r'<a href="(http://www.51ape.com/ape/\d*.html)" class="wm210 c3b fl f_14 over t20d ml_1" title="(%s.*)">(.*)</a>' % (artist)
						results = self.spiderPage(page, reString)
						i = 1
						for m in results :
							tempUrl = m.group(1)
							title = m.group(2)
							musicName = m.group(3)
							#print(tempUrl, title, musicName)
							panUrl, pwd = self.getMusicUrl(tempUrl,title, musicName, artist)
							try:
								sql = "insert into music(`title`, `musicName`, `artist`, `url`, `password`) values('%s', '%s', '%s', '%s', '%s');" % (title, musicName, artist, panUrl, pwd)
								self.dao.launchSQL(sql)
								print sql
							except:
								print("encode fail", tempUrl, title, musicName, artist)
								print(chardet.detect(tempUrl), chardet.detect(title), chardet.detect(musicName), chardet.detect(artist))
							time.sleep(1)
							print(i)
							i = i + 1
			else:
				reString = r'<a href="(http://www.51ape.com/ape/\d*.html)" class="wm210 c3b fl f_14 over t20d ml_1" title="(%s.*)">(.*)</a>' % (artist)
				results = self.spiderPage(page, reString)
				for m in results :
					tempUrl = m.group(1)
					title = m.group(2)
					musicName = m.group(3)
					#print(tempUrl, title, musicName)
					panUrl, pwd = self.getMusicUrl(tempUrl,title, musicName, artist)
					try:
						sql = "insert into music(`title`, `musicName`, `artist`, `url`, `password`) values('%s', '%s', '%s', '%s', '%s');" % (title, musicName, artist, panUrl, pwd)
						self.dao.launchSQL(sql)
						print sql
					except:
						print("encode fail", tempUrl, title, musicName, artist)
						print(chardet.detect(tempUrl), chardet.detect(title), chardet.detect(musicName), chardet.detect(artist))
					time.sleep(1)

	def getMusicUrl(self, url, title, musicName, artist):
		page = self.GET(url)
		if type(page) == type('a') :
			reString1 = r'''<a href="(http://pan.baidu.com/.*)" title=".*" rel="nofollow" target="_blank" class="blue a_none"><h2 class="bg_gr b_b_s m_s logo mt_1 yh white" style=".*">高速下载</h2></a>'''
			tempResult1 = self.spiderPage(page, reString1)
			panUrl = None
			pwd = None

			for tempM in tempResult1 :
				print(tempM.group(1))
				panUrl = tempM.group(1)

			reString2 = r'''<b class="mt_1 yh d_b" style=".*">提取<em class="dn"></em>密码：(.*)</b>'''
			tempResult2 = self.spiderPage(page, reString2)

			for tempM in tempResult2 :
				print(tempM.group(1))
				pwd = tempM.group(1)
			print("----------A---------")
			return panUrl, pwd



if __name__ == '__main__':
	spider = Spider()
	# url = "http://www.baidu.com/"
	# data = {"name":"123", "pwd":"123"}
	# page = spider.GET(url, None, data)
	# print(page)
	# url = "http://www.51ape.com/artist/"
	# reString = r'<div class="gs_a"><a href="(http://www.51ape.com/\w*/)" class="c47 f_14 b yh">(.*)</a></div>'
	# spider.spiderUrl(url, reString)
	url = "http://www.51ape.com/jay/"
	spider.getArtistMuisc(url, "周杰伦")