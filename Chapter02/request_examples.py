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