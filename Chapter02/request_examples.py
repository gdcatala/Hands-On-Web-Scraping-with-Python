import requests

link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
# The .get() method returns "Response" object
response = requests.get(link)
# The response.content method retreives a byte object
content = response.content
# The response.txt method retreives  a string object
content_string = response.text

with open("wikipedia_content", "w") as file:
    file.write(content_string)

#The following are some request attributes, along with a short expla
#tion of each: (i) url outputs the current URL, (ii) the HTTP status
# code is found using status_code

print(f"Status Code: {response.status_code}")

#Through the GET method the resource state is not altered. The GET
#parameters, also known as query strings, are visible in the URL.
#They are appended to the URL using ? and are available as key=value pairs

link2 = "http://localhost:8080/~cache"
queries = {"id":"123456", "display":"yes"}
addedheaders = {"user-agent":""}

#r1 = requests.get(link2, params=queries, headers=addedheaders)
#print(r.url)

#Through the POST method the resource state can be altered.