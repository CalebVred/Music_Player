from Track_dLoader import Track_dLoader


#Subscribes to Roosh V's RSS feed through feedburner
print("dLoader1: Testing 'https://feeds.feedburner.com/dcb'")
dLoader1 = Track_dLoader("https://feeds.feedburner.com/dcb", "Roosh Hour", "~/Downloads")
dLoader1.dLoadEList()
assert(len(dLoader1.getEList()) > 0)
print("dLoader1 Episode List not empty")
latest_ep = dLoader1.getEList()[0]
print("Latest episode title:", latest_ep.title)
#print("Latest episode description:", latest_ep.description)
print("Latest episode link:", latest_ep.link)
#dLoader1.openAndDownload(latest_ep)

#Downloads the latest episode of the WAN show
print("dLoader2: Testing 'https://www.youtube.com/feeds/videos.xml?channel_id=UCXuqSBlHAE6Xw-yeJA0Tunw'")
dLoader2 = Track_dLoader("https://www.youtube.com/feeds/videos.xml?channel_id=UCXuqSBlHAE6Xw-yeJA0Tunw",
                         "WAN Show", "~/Downloads")
dLoader2.dLoadEList()
assert(len(dLoader2.getEList()) > 0)
print("dLoader2 Episode List not empty")
latest_ep = dLoader2.getEList()[0]
print("Latest episode title:", latest_ep.title)
#print("Latest episode description:", latest_ep.description)
print("Latest episode link:", latest_ep.link)
dLoader1.dLoadYT(latest_ep)
