#!/usr/bin/python
# -*- coding: utf8 -*-

# TODO
# surround with try/catch

import sqlite3
from url import Url

class Dbler:
	def __init__ (self, dbname):
		self.createdb(dbname)
		self.url_id = 0

	def createdb(self, dbname):
		#TODO: check if db already exists
		self.con = sqlite3.connect(dbname)
		c = self.con.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS url_base
					(scheme TEXT,
					netloc TEXT,
					path TEXT,
					ftype TEXT,
					PRIMARY KEY(scheme, netloc, path))''')
		# TODO: add query column (?)
		c.execute('''CREATE TABLE IF NOT EXISTS url_full
					(url TEXT PRIMARY KEY, 
					url_base_id INTEGER NOT NULL,
					FOREIGN KEY(url_base_id) REFERENCES url_base(rowid))''')
		c.execute('''CREATE TABLE IF NOT EXISTS link
					(src TEXT,
					dst TEXT,
					PRIMARY KEY(src,dst),
					FOREIGN KEY(src) REFERENCES url_full(url),
					FOREIGN KEY(dst) REFERENCES url_full(url))''')
		c.execute('''CREATE TABLE IF NOT EXISTS param_name
					(name TEXT,
					url_base_id INTEGER,
					PRIMARY KEY(name, url_base_id),
					FOREIGN KEY(url_base_id) REFERENCES url_base(row_id))''')
		c.execute('''CREATE TABLE IF NOT EXISTS param_value
					(name TEXT,
					value BLOB,
					PRIMARY KEY(name, value),
					FOREIGN KEY(name) REFERENCES param_name(name))''')
		self.con.commit()
		c.close()

	def addUrls(self, urls, origin=None):
		c = self.con.cursor()
		for url in urls:
			u = Url(url)
			c.execute('''INSERT OR IGNORE INTO url_base(rowid,scheme,netloc,path,ftype)
						VALUES(?,?,?,?,?)''', \
								(self.url_id, u.scheme, u.netloc, u.path, u.ftype))
			c.execute('''INSERT OR IGNORE INTO url_full(url, url_base_id)
						VALUES(?,?)''', (url, self.url_id))
			if origin:
				c.execute('''INSERT  OR IGNORE INTO link(src,dst)
							VALUES(?,?)''', (url, origin))
			for name, value in u.args.items():
				c.execute('''INSERT OR IGNORE INTO param_name(name, url_base_id)
							VALUES(?,?)''', (name, self.url_id))
				c.execute('''INSERT OR IGNORE INTO param_value(name, value)
							VALUES(?,?)''', (name, value))
			self.url_id = self.url_id + 1
		# TODO: meight wanna use rowid functionality here
		self.con.commit()
		c.close()

	def addUrl(self, url, origin=None):
		c = self.con.cursor()
		u = Url(url)
		c.execute('''INSERT OR IGNORE INTO url_base(rowid,scheme,netloc,path,ftype)
						VALUES(?,?,?,?,?)''', \
								(self.url_id, u.scheme, u.netloc, u.path, u.ftype))
		c.execute('''INSERT OR IGNORE INTO url_full(url, url_base_id)
					VALUES(?.?)''', (url, self.url_id))
		if origin:
			c.execute('''INSERT OR IGNORE INTO link(src,dst)
						VALUES(?,?)''', (url,origin))
		for name, value in u.args.items():
			c.execute('''INSERT OR IGNORE INTO param_name(name, url_base_id)
						VALUES(?,?)''', (name, self.url_id))
			c.execute('''INSERT OR IGNORE INTO param_value(name, value)
						VALUES(?,?)''', (name, value))
		# TODO: meight wanna use rowid functionality here
		self.url_id = self.url_id + 1
		self.con.commit()
		c.close()
	
	def close(self):
		self.con.close()
