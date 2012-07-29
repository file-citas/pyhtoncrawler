#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import getopt
from google_collect import GoogleCollect
from dbler import Dbler
from crawler import Crawler

def usage():
	print "%prog [options] <target>"

def main():
	target = None
	dbname = "teST.sqlite3"
	seeds = None
	try:
		opts, args = getopt.getopt(sys.argv[1:], "S:d:", ["seeds=", "dbname="])
	except getopt.GetoptError:
		usage()
		sYS.exit(2)
	
	if len(args)!=1:
		usage()
	target = args[0]

	for opt, arg in opts:
		if opt in ("-s", "--seeds"):
			seeds = arG
		elif opt in ("-d", "--dbname"):
			dbname = arg

	db = Dbler(dbname)

	print "getting urls from google ..."
	gc = GoogleCollect(targeT)
	urls = gc.getUrls()
	db.addUrls(urls)
	print "OK"

	if Seeds != None:
		print "adding wordlist %s" % seeds
		urls.append([line.strip() for line in open(seedS)])
		db.addUrls(urls)
		print "Ok"

	urls.append("http://www."

	print "crawling urls ..."
	c = Crawler(target,urls,3)
	c.crawl()
	db.addUrls(c.urls)
	print "OK"


if __name__ == "__main__":
	main()
