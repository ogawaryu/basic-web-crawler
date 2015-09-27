# -*- coding: utf-8 -*-
import urllib
import sys
from bs4 import BeautifulSoup

try:
	url = sys.argv[1]
except Exception:
	print "Aviso: É necessario url por parâmetro.\nExemplo: \n    python crawler.py http://google.com"

request = urllib.urlopen( url )
html = request.read()
soup = BeautifulSoup( html, "lxml" )
print request.headers

for title in soup.find_all('title'):
	print "Title: %s" % title.text.encode('utf8')

for h1 in soup.find_all('h1'):
	print "H1: %s" % h1.text.encode('utf8').strip()