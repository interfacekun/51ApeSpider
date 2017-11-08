# -*- coding: utf-8 -*-
##[[
 # @brief:		main.py

 # @author:		kun si
 # @email:	  	627795061@qq.com
 # @date:		2017-11-07
##]]

from dao import Dao
from spider import Spider

if __name__ == '__main__':
	dao = Dao()
	spider = Spider()
	dao.connect()

	url = "http://www.51ape.com/artist/"
	reString = r'<div class="gs_a"><a href="(http://www.51ape.com/\w*/)" class="c47 f_14 b yh">(.*)</a></div>'

	resultsList = spider.getArtistUrl(url, reString)

	for m in resultsList:
		sql = "insert into artist(`artist`, `url`) values('%s', '%s');" %(m.group(2), m.group(1))
		dao.launchSQL(sql)