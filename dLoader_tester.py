from Podcast_DLoader import Track_dLoader


#Downloads the latest episode of the WAN show using RSS URL
print("dLoader1a: Testing 'https://www.youtube.com/feeds/videos.xml?channel_id=UCXuqSBlHAE6Xw-yeJA0Tunw'")
dLoader1a = Track_dLoader("https://www.youtube.com/feeds/videos.xml?channel_id=UCXuqSBlHAE6Xw-yeJA0Tunw",
                         "WAN Show", "Downloads")
assert(len(dLoader1a.getEList()) > 0)
print("dLoader1a Episode List not empty")
latest_ep = dLoader1a.getEList()[0]
print("Latest episode title:", latest_ep.title)
#print("Latest episode description:", latest_ep.description)
print("Latest episode link:", latest_ep.link)
dLoader1a.dLoadYT(latest_ep)

#Downloads the latest episode of the WAN show using html URL
#Downloads the latest episode of the WAN show using RSS URL
print("dLoader1b: Testing 'https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw'")
dLoader1b = Track_dLoader("https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw",
                         "WAN Show", "Downloads")
assert(len(dLoader1b.getEList()) > 0)
print("dLoader1b Episode List not empty")
latest_ep = dLoader1b.getEList()[0]
print("Latest episode title:", latest_ep.title)
#print("Latest episode description:", latest_ep.description)
print("Latest episode link:", latest_ep.link)
dLoader1b.dLoadYT(latest_ep)
