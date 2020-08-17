from Track_dLoader import Track_dLoader
#Subscribes to Roosh V's RSS feed
print("dLoader1: Testing 'https://feeds.feedburner.com/dcb'")
dLoader1 = Track_dLoader("https://feeds.feedburner.com/dcb", "Roosh Hour")
dLoader1.dLoadEList()
assert(len(dLoader1.getEList()) > 0)
print("dLoader1 Episode List not empty")
print("Latest episode:", dLoader1.getEList()[0].title)
print("Oldest available episode:", dLoader1.getEList()[-1].title)