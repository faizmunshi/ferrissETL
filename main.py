#!/usr/bin/python
import urllib
import xmltodict
import unicodecsv
import re
from bs4 import BeautifulSoup

import json

FEED_URL = 'https://feeds.feedburner.com/thetimferrissshow'
FEED_FILE = 'rss.xml'
CSV_FILE = 'extract.csv'
# AUDIO_BOOK_PATTERN = '<a href= "http://www.audible.com'

findings = {}

print "Fetching HTML"
urllib.urlretrieve (FEED_URL, FEED_FILE)

with open(FEED_FILE) as fd:
    doc = xmltodict.parse(fd.read())


#scrape podcast links and extract relevant links for each podcast page
page = urllib.urlopen("http://fourhourworkweek.com/podcast/").read()
# print page
podcastLinks = BeautifulSoup(page, "html.parser")
# print(podcastLinks.find_all('a'))
for link in podcastLinks.find_all(class_='podcast'):
        # if link != "None":
        # if link.get('href').find("amazon") > 1:
            print link.find('a').get('href')
            pPage = urllib.urlopen(link.find('a').get('href')).read()
            podcastPage = BeautifulSoup(pPage, "html.parser")
            for link in podcastPage.find_all(href=re.compile("amazon")):
            #     if link.get('href').find("amazon") > 1:
                    print link



#needs editing
for item in doc['rss']['channel']['item']:
    	findings[item['title']] = item['description']
    	soup = BeautifulSoup(item['description'], "html.parser")
        # print(soup.find('a'))
    	findings[item['title']] = []
    	# link_enum = 0

        for link in soup.find_all('a'):
            # print(link.get('href'))
            if link.get('href').find("amazon") > 1:
                # findings[item['title']][link_enum] = {}
                findings[item['title']].append(link.get('href'))
                # findings[item['title']][link_enum]['type'] = 'Book?'
                # link_enum += 1
                # print link.get('href')
            # if link.get('href').find('audible') > 1:
            #     findings[item['title']][link_enum] = {}
            #     findings[item['title']][link_enum]['link'] = link.get('href')
            #     findings[item['title']][link_enum]['type'] = 'Audiobook?'
            #     link_enum += 1
            #     print link.get('href')


with open(CSV_FILE, 'w') as csvfile:
    	fieldnames = ['Episode', 'Description']
    	writer = unicodecsv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()

        for ep in findings:
            for link in findings[ep]:
                writer.writerow({'Episode': ep, 'Description':link})


#if removing the below, remove import
# print json.dumps(findings)
