# The urllib.error deals with the exceptions raised by the urllib.request.
# The folllowing code demonstrates how to use this library.

import urllib.request as request
import urllib.error as error
import urllib.parse as urlparse

try:
    request.urlopen("https://www.python.ogr")
except error.URLError as e:
    print("Error Occurred: ",e.reason)

# The urllib.parse is used to encode/decode request or links and analyze, add
# update headers, parse, and manipulate URLs.

amazonUrl = 'https://www.amazon.com/s/ref=nb_sb_noss?' \
            'url=search-alias%3Dstripbooks-intl-ship&field-keywords=' \
            'Packt+Books'

# The .urlsplit() function splits the URLs that's passed into a namedtuple
# object where each name in tuple identifies parts of the URL.

print(urlparse.urlsplit(amazonUrl))
Query = urlparse.urlsplit(amazonUrl).query
print(f"Query: {Query}")
Scheme = urlparse.urlsplit(amazonUrl).scheme
print(f"Scheme: {Scheme}")

# There is another functions similar to .urlsplit() called .urlparse() that
# creates ParseResult object. It differs from the former in splitting the URL
# in more substring including one called "params", that in this particular case
# is empty.

print(urlparse.urlparse(amazonUrl))

# In order to request data, Query Information, or URL arguments need to be used
# as key-value pair of information that are appended to the desired URL. Query
# information that's passed to the request object should be encoded using
# urlencode() function.

# The .urlencode() method ensures that arguments comply with the W3C standard
# and are accepted by the server.

data = {'param1': 'value1', 'param2': 'value2'}
print(urlparse.urlencode(data))
print(urlparse.urlencode(data).encode("utf-8"))




