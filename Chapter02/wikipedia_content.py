import requests

link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = requests.get(link)
#*print(type(response))
# the response.content method retreives a byte object
#*content = response.content
# the response.txt method retreives  a string object
content_string = response.text
#*print(content[0:150])

with open("wikipedia_content", "w") as file:
    file.write(content_string)