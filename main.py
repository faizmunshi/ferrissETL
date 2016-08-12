import urllib

FEED_URL = 'https://overcast.fm/itunes863897795/the-tim-ferriss-show'

print "Fetching XML"
urllib.urlretrieve (FEED_URL, "rss.xml")

