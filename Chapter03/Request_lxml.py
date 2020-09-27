#In this example, we will be reading a URL, which contains HTML-based
#form elements. Form elements have various predefined attributes such as
#type, value, name and can exist eith manual attributes.

from lxml import html
import requests

#Here, we will try to collect the attributes and their values found in
#HTML-form elements

response = requests.get('http://httpbin.org/forms/post')
print(type(response))
print(type(response.text))


#The .fromstring() function parses the provided string object and
#returns the root node or the HTMLElement tree type

tree = html.fromstring(response.text)
print(type(tree))

#In this example, we are iterating the input element and are looking
#to identify  the attributes each input possesses

for element in tree.iter('input'):
    print("Element: %s \n\tvalues(): %s \n\tattrib: %s \n\titems(): %s \n\tkeys(): %s"%
        (element.tag, element.values(),element.attrib,element.items(),element.keys()))
    print("\n")

#element.tag: returns the element tag name

#element.values(): The attributes of HTML form element exist as key: value
#pair. The value attribute holds the exact data for the particular element.
#values() returns the value attribute for the chosen element in the list object

#element.attrib: returns a Dict type object with a key:value pair

#element.items(): returns a list object with a tuple possessing a key and value

