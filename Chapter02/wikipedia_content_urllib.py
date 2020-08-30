import urllib.request as req
import os
link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = req.urlopen(link)
print(type(response))
print(response.read())

