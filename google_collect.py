#!/usr/bin/python

from xgoogle.search import GoogleSearch, SearchError

class GoogleCollect:
	def __init__(self, target):
		self.target = target
		self.urls = []
		self.collect()

	def collect(self):
		gs = GoogleSearch("site:"+self.target)
		while True:
			results = gs.get_results()
			for res in results:
				self.urls.append(res.url.encode('utf8'))
			if len(results)<10:
				break

	def getUrls(self):
		return self.urls
