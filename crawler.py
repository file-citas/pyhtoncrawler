#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from google_collect import GoogleCollect
from dbler import Dbler

def main():
	db = Dbler('test.sqlite3')
	gc = GoogleCollect(sys.argv[1])
	urls = gc.getUrls()
	db.addUrls(urls)

if __name__ == "__main__":
	main()
