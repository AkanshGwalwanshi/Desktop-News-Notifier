import requests
import xml.etree.ElementTree as ET

URL = "http://timesofindia.indiatimes.com/rssfeedstopstories.cms"

def loadRSS():
    
    # creating https request's response object
    resp = requests.get(URL)

    return resp.content

# function to parse xml
def parseXML(rss):

    # creating element tree's root object
    root = ET.fromstring(rss)

    newsItems = []

    # iterate news items
    for item in root.findall('./channel/item'):
        news={}

        for child in item:

            if child.tag == 'http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                try:
                    news[child.tag] = child.text.encode('utf8')
                
                except AttributeError:
                    pass

        newsItems.append(news)

    return newsItems


def topNews():
    
    rss = loadRSS()

    newsItems = parseXML(rss)

    return newsItems

