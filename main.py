#!/usr/bin/python
import urllib
import xmltodict

FEED_URL = 'https://feeds.feedburner.com/thetimferrissshow'
FEED_FILE = 'rss.xml'
# AUDIO_BOOK_PATTERN = '<a href= "http://www.audible.com'

print "Fetching XML"
urllib.urlretrieve (FEED_URL, FEED_FILE)

with open(FEED_FILE) as fd:
    doc = xmltodict.parse(fd.read())

print doc