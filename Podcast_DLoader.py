import feedparser
import re
import sys
from pytube import YouTube
import os
import platform

from selenium import webdriver
from selenium.webdriver import Chrome
#from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver import ActionChains



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
       
        opt = webdriver.ChromeOptions()
        opt.binary_location = "~/chromedriver"
        #Selenium
        #self.driver = webdriver.Chrome(chrome_options=opt, executable_path='~/chromedriver')
        #TODO: This triggers an error

    #Retrieves a list of podcast episodes from RSS feed
    def dLoadEList(self):
        feed = feedparser.parse(self.feedURL)
        
        #Appends to self.episodeList RSS entries that contain the show title
        for entry in feed.entries:
            if(self.containsTitle(entry.title, self.showTitle)) != -1:
                self.episodeList.append(entry)

    
    #Retrieve local episode list
    def getEList(self):
        return self.episodeList

                       
    #Searches the string RSS item title itemT for substring show title showT
    #Returns 0 if the title is present or the episode number if available
    #Returns -1 if the title is not present
    def containsTitle(self, entryT, showT):
        search = entryT.find(showT)
        if search != -1:
            return 0
        else:
            return -1
    
    #Download YouTube video an RSS feed item that links to a YouTube video
    def dLoadYT(self, episode):
        try:
            YouTube(episode.link).streams.first().download(self.dest)
        except:
            print("Connection Error: link might be invalid or video could be removed")

    
            
    '''
    #Open the link with Selenium
    def openAndDownload(self, episode):
        #TODO: May need to make separate API for handling Zencast modules
        
        actions = ActionChains(self.driver)
        #Follow the episode link
        self.driver.get(episode.link)
        shareButtonXPath = "/html/body/div[2]/div/div/div[3]/div/div[1]/button[3]"
        shareButton = self.driver.find_element_by_xpath(shareButtonXPath)
        actions.click(shareButton)

        dLoadButtonXPath = "/html/body/div[2]/div/div/div[3]/div[1]/div[2]/h6"
        dLoadButton = self.driver.find_elements_by_xpath(dLoadButtonXPath)
        actions.context_click(dLoadButton).perform()
    '''