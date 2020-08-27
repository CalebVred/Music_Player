import feedparser
import re
import sys
from pytube import YouTube
#from moviepy.editor import *
import os
import platform

#Track_dLoader class takes in a source (RSS) feed and finds
#and downloads the latest episode based on the show title
class Track_dLoader:
    #Initialize
    def __init__(self, feedURL, showTitle, dest):
        #feedparser
        self.episodeList = []
        self.feedURL = feedURL
        self.showTitle = showTitle
        self.dest = dest
       
        #opt = webdriver.ChromeOptions()
        #opt.binary_location = "~/chromedriver"
        #Selenium
        #self.driver = webdriver.Chrome(chrome_options=opt, executable_path='~/chromedriver')
        #TODO: This triggers an error
        
        #Handle YouTube links
        if (re.search(r'youtube.com', self.feedURL)):
            self.feedURL = self.handleYTLink(self.feedURL)

        #Retrieve podcast episode list
        self.dLoadEList()  
        
    
    #Input: url(str), a link to a YouTube channel in HTML or RSS xml form
    #Output: rssURL, a proper RSS-friendly URL
    #Converts html address of YouTube channel to RSS address
    def handleYTLink(self, url):
        
        #If HTML prefix is present, search for it and replace it with the RSS prefix
        rss = re.compile(r'https://www.youtube.com/channel/')
        rssURL = rss.sub(r'https://www.youtube.com/feeds/videos.xml?channel_id=', url)
        
        return rssURL
    
    #Input: None
    #Output: None
    #Retrieves a list of podcast episodes from RSS feed
    def dLoadEList(self):
        feed = feedparser.parse(self.feedURL)
        
        #Appends to self.episodeList RSS entries that contain the show title
        for entry in feed.entries:
            if(self.containsTitle(entry.title, self.showTitle)) == True:
                self.episodeList.append(entry)

    #Input: None
    #Output: self.episodeList (List)
    #Retrieves local episode list
    def getEList(self):
        return self.episodeList

    #Input: None
    #Output: True if the title is present or the episode number if available
    #Returns False if the title is not present
    #Searches the string RSS item title itemT for substring show title showT
    def containsTitle(self, entryT, showT):
        search = entryT.find(showT)
        if search != -1:
            return True
        else:
            return False
    
    #Input: episode
    #Output: None
    #Downloads YouTube video to destination directory 
    def dLoadYT(self, episode):
        #Download YouTube video or throw error
        try:
            YouTube(episode.link).streams.first().download(self.dest)
        except:
            print("Connection Error: link might be invalid or video could be removed")



    