#!/usr/bin/python

import sys
from xgoogle.search import GoogleSearch, SearchError

class GoogleCrawl:
	def __init__(self, target):
		self.target = target
		self.urls = []
		self.crawl()

	def crawl(self):
		gs = GoogleSearch("site:"+self.target)
		while True:
			results = gs.get_results()
			if len(results)<10:
				break
			for res in results:
				self.urls.append(res.url.encode('utf8'))

	def getUrls(self):
		return self.urls

def main():
	print 
	gc = GoogleCrawl(sys.argv[1])
	urls = gc.getUrls()
	for url in urls:
		print url

if __name__ == "__main__":
	main()
