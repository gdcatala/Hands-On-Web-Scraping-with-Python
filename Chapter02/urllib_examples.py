import urllib.request as req
import sys

link1 = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
link2 = "http://www.dce.com.cn/webquote/futures_quote_en.jsp?varietyid=I"

# The .urlopen() function returns a HTTPResponse object

linkResponse = req.urlopen(link1)

# The .read() on a HTTPResponse object returns a bytes object

linkRequest = req.urlopen(link1).read()

# There is another function called Request(), that returns a Resquest ojects.
# This functions is generally used to send extra arguments like data, headers
# and even to specify the HTTP method and retrieve a response

requestObj = req.Request(link2)

# The Request object can be used as an argument for the .urlopen() function to
# get an bytes object

requestObjResponse = req.urlopen(requestObj).read()

with open("url_request", "wb") as file:
    file.write(requestObjResponse)

# The .getcode() function returns the HTTP status code. If the request was made
# successful and received a response from the proper URL the code will be 200

status = linkResponse.getcode()
print(f" Connection Status: {status}")

# The .geturl() method returns a list with tuples that contains HTTP headers.
# We can determine values regarding cookie, content type, date and so on

headers = linkResponse.getheaders()
print(f"Headers: {headers}")

# Individual headers can be retreived when the .getheader() method  is passed
# with the desired header element name

charset = linkResponse.getheader("Content-Type")
print(f"Charset: {charset}")


