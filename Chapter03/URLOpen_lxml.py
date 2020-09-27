#In this example we will be using the lxml.html module to traverse
#through the elements from http://httpbin.org/forms/post

from lxml import html
from urllib.request import urlopen

#We are using "parse()" method from lxml.html to load the given URL content
#The parse() acts similarly to lxml.etree but, in this case, root obtained is
#of the HTML type

URL = "http://httpbin.org/forms/post"
root = html.parse(urlopen(URL)).getroot()
tree = html.parse(urlopen(URL))

#In this example we are interested in root or HTMLElement

print(type(root))
print(type(tree))

#Let's find <p> from root; "find()" method can be used to locate
#the first elemt by path. Text can be retrieved using the
#text_content()

p = root.find(".//p")
print(p.text_content())

#The "findall()"method is used to find and iterate through all
#elements in the root

elemP = root.findall(".//p")
for a in elemP:
    print(a.text_content())

#The HTMLElement root also supports XPath and CSSSelect

print(root.xpath("//p/label/input/@value"))
print(root.xpath("//legend/text()"))

#CSSSelect translates CSS selectors into XPath expressions
#and is used with a related object:

for e in root.cssselect("p label"):
    print(e.text_content())

#The following snippet print the text_content for element <p>
#inside <form>

for e in root.cssselect("form > p"):
    print(e.text_content())

#The following code demostrate the HTML <form> element being explore
#for its attributes and properties. We are targeting the <form> element
#first, which is found in root

print(root.forms[0].action)
print(root.forms[0].keys())
print(root.forms[0].items())
print(root.forms[0].method)



















