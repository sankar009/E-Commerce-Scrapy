def getURL():
	start_urls=list()
	for i in range(1,120):
	    tempUrl="http://www.jabong.com/women/clothing/tops-tees-shirts/?source=topnav_women&ax=1&page="+str(i)+"&limit=100&sortField=popularity&sortBy=desc"
	    start_urls.append(tempUrl)
	return start_urls