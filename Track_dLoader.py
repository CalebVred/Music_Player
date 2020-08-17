import feedparser
import re
#import sys
#from selenium import webdriver
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options

#Track_dLoader class takes in a source (RSS) feed and finds
#and downloads the latest episode
class Track_dLoader:
    #Initialize
    def __init__(self, feedURL, showTitle):
        self.episodeList = []
        self.feedURL = feedURL
        self.showTitle = showTitle
    
    #Retrieves a list of podcast episodes from RSS feed
    def dLoadEList(self):
        feed = feedparser.parse(self.feedURL)
        
        for item in feed.entries:
            if(self.containsTitle(item.title, self.showTitle)) != -1:
                self.episodeList.append(item)

    #Retrieve local episode list
    def getEList(self):
        return self.episodeList

                       
    #Searches the string RSS item title itemT for substring show title showT
    #Returns 0 if the title is present or the episode number if available
    #Returns -1 if the title is not present
    def containsTitle(self, itemT, showT):
        #TODO: change this to accomodate episode number
        showTemplate = re.compile(showT)
        search = showTemplate.search(itemT)
        if search:
            return 0
        else:
            return -1
    
    #Open the link with Selenium
    #def openAndDownload():
        #TODO: May need to make separate API for handling Zencast modules