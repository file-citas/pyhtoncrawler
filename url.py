#!/usr/bin/python
# -*- coding: utf8 -*-

import cgi, urllib, urlparse
import os
import urlnorm

class Url(object):
	"""A structured URL.

	Create from a string or Django request, then read or write the components
	through attributes `scheme`, `netloc`, `path`, `params`, `query`, and
	`fragment`.

	The query is more usefully available as the dictionary `args`.

	"""
	def __init__(self, url):
		"""Construct from a string or Django request."""
		nurl = urlnorm.norm(url)
		if hasattr(nurl, 'get_full_path'):
			nurl = nurl.get_full_path()

		self.scheme, self.netloc, self.path, self.params, \
			self.query, self.fragment = urlparse.urlparse(nurl)
		filename, self.ftype = os.path.splitext(self.path)
		self.args = dict(cgi.parse_qsl(self.query))

	def __str__(self):
		"""Turn back into a URL."""
		self.query = urllib.urlencode(self.args)
		return urlparse.urlunparse((
			self.scheme, self.netloc, self.path, self.params,
			self.query, self.fragment
			))
