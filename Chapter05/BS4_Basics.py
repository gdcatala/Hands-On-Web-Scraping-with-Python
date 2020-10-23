##################################Introduction to BS4############################################
#Beautiful Soup generates a parsed tree similar to lxml (ElementTree), which is used to identify and
#traverse through elements to extract data and perform web scraping.
#One of the distinguishing features of Beautiful Soup, over other libraries and parsers, is that it can
#also be used to parse broken HTML or files with incomplete or missing tags.

#The Python BS4 library contains a BeautifulSoup class, which is used to parsing.

from bs4 import BeautifulSoup,SoupStrainer
import re

#We will be using the following HTML as an example to explore some fundamental features of Beautiful Soup
#The response obtained for any chosen URL using request can also be used to content in real scrapind cases

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<h1>Secret agents</h1>
<ul>
    <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
    <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in "Goldeneye".</li>
    <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
</ul>
</body>
</html>
"""

#To proceed with parsing and accessing Beautiful Soup methods and properties, a Beautiful Soup object,
#generally known as a soup object must be created. There are several options to create a Beautiful Soup
#object:
#(i) soup = Beautifulsoup(html_markup)
#(ii) soup = Beautifulsoup(html_markup, "lxml")
#(iii) soup = Beautifulsoup(html_markup, "lxml", parse_from=Soup-Strainer("a"))

#The Beautiful Soup constructor plays an important part and we will explore some of the important parameter
#her:
#(i) markup: The first parameter passed to the constructor accepts a string or objects to be parsed
#(ii) features: The name of the parser ot type of markup to be used for markup. The parser can be lxml,
#lxml-xml, html.parser, or html15. If we just want to parse some HTML, we can simply pass the markup to
#BeautifulSoup and it will use the appropriate parser installed accordingly.
#(iii) parse_only: Accepts a bs4.SoupStrainer object, that is, only parts of the document matching the
#SoupStrainer object will be used to parse.

#In this example we will be creating the soupA object using lxml as a parser, along with the SoupStrainer
#object tagsA-> parsing only <a>,that is, the elements or anchor tag of HTML

tagsA = SoupStrainer("a")
soupA = BeautifulSoup(html_doc,'lxml',parse_only=tagsA)
soup = BeautifulSoup(html_doc,'lxml')

#The .pretiffy() function returns a Unicode string, presents the string in a clean, formatted structure
#that is easy to read

soupA #print
soupA.prettify() #print

#Document-based elements (such as HTML tags) in a parsed tree can have various attributes with predefined
#values. Verifying whether the element contains certain attributes can be handy when traversing the tree
#Remember->soupA.a returns the first <a> element or tag found in the html_doc

soupA.a.has_attr("class")
soupA.a.has_attr("name")
soupA.a.has_attr("href")
soupA.a.has_attr("id")

#The .find() function returns the first child that is matched for the searched criteria or parsed element.
#Additional parameters can also be passed to the .find() function to identify the exact element:
#(i) attrs: A dictionary with a key-value pair
#(ii) text: with element text
#(iii) name: HTML tag name

#.find("a"): Search the HTML <a> element or tag name provided. Returns the first existence of <a> found
#in soupA
#.find("a", attrs={"class":"sister"}, text="Lacie"): Search element <a> with the class attribute key and
#the sister value and text with the Lacie value

#THE .FIND() RETURNS A TAG ELEMENT, WHICH CONTAINS EVERY CHILD TAGS OR STRINGS

soupA.find("a")
soupA.find("a",attrs={'class':'sister'})
soupA.find("a",attrs={'class':'sister'},text="Lacie")
soupA.find("a",attrs={'id':'link3'})
soupA.find('a',id="link2")

#The .find_all() function works in a similar way to the .find() function with the additional attrs and
#text as a parameters and returns a list of matched (multiple) elements for the provided criteria or
#name attribute

soupA.find_all("a")

#The additional limit parameter, which accepts numeric values, controls the total count of the elements
#to be returned using the find_all() function

soupA.find_all("a",limit=2)

#The following snippet is related to regular expressions

soupA.find("a",text=re.compile(r'cie'))
soupA.find_all("a",attrs={'id':re.compile(r'3')})
soupA.find_all(re.compile(r'a'))

#The .find_all() function has in-built support for global attributes such as class name along with a
#name as seen in the following

soup = BeautifulSoup(html_doc,'lxml')
soup.find_all("p","story") #class=story
soup.find_all("p","title") #soup.find_all("p",attrs={'class':"title"})

#Finding all the <p> elements with the class attribute "title" and "story" values

soup.find_all("p",attrs={'class':["title","story"]})

#Finding all the <p> and <li> elements from the soup object

soup.find_all(["p","li"])

#We can also use element text to search and list the content. A "string" parameter, similar to a "text"
#parameter, is used for such cases. It can be used with, or without, any tag name as in the following
#code:

soup.find_all(string="Elsie") #you can also use text="Elsie"
soup.find_all(text=re.compile(r'Elsie')) #import re
soup.find_all("a",string="Lacie") #text="Lacie"

#Iteration through elements can also be achieved using the find_all() function. We are retireving all
#of the <li> elements found inside the <ul> element and their tag name, attribute data, ID and text
#We can iterate because the .find_all() function returns a list object

#for li in soup.ul.find_all('li'):
#    print(li.name, ' > ',li.get('data-id'),' > ', li.text)

#Element traversing can also be done with just a tag name, and with, or without, using find() or
#find_all() functions as seen in the following code:

soupA.a #tag a
soup.li #tag li
soup.p
soup.p.b #tag p and b
soup.ul.find('li',attrs={'data-id':'45732'})

#The text and string attributes or the get_text() method can be used with the elements to extract their
#text while traversing through the elements used in the following code.

soup.ul.find('li',attrs={'data-id':'45732'}).text
soup.p.text #get_text()
soup.li.text
soup.p.string

#################################USING CHILDREN AND PARENTS#############################################

#For parsed document, traversing through children or child elements can be achieved using:
#(i) contents: collect children for the provided criteria in a list
#(ii) children: are used for iteration that has direct children
#(iii) descendents: it allows iteration over all children, not just the direct ones

list(soup.find('p','story').children) #Is a list_iterator object
list(soup.find('p','story').contents) #Is a list_iterator object
list(soup.find('p','story').descendants) #Is a list_iterator object

#Selected children and descendants tag names can be obtained using the name attribute. Parsed strings
#and the \n function (newline) are returned as "None", which can be filtered out

[a.name for a in soup.find('p','story').children]
[{'tag':a.name,'text':a.text,'class':a.get('class')} for a in soup.find('p','story').children if a.name!=None]
[a.name for a in soup.find('p','story').descendants]
list(filter(None,[a.name for a in soup.find('p','story').descendants]))

#Similar to the .find() and .fin_all() functions, we can also traverse child elements using the
#the .findChild()->just a single element and .findChildren()->returns a list .

soup.find('p','story').findChildren() #Is a list object
soup.find('p','story').findChild() #Is a list object

#The main difference with the .parent() function is that it returns a single parent object from the tree:

soup.find('a','sister').parent

#print parent element name of <a> with class=sister

soup.find('a','sister').parent.name

#print text from parent element of <a> with class=sister

soup.find('a','sister').parent.text

#The limitation of the single parents returned can be overcome by using the "parents" elements; this
#returns multiple existing parent elements and matches the searched criteria provided in the .find()
#function

#for element in soup.find('a','sister').parents:
    #print(element.name)
	
#find single Parent for selected <a> with class=sister 

soup.find('a','sister').findParent()

#find Parents for selected <a> with class=sister 
print(soup.find('a','sister').findParents())

print(soup.find('p','story').next)

print(soup.find('p','story').next.next)

print(soup.find('p','story').next_element)

print(soup.find('p','story').next_element.next_element)

print(soup.find('p','story').next_element.next_element.next_element)

print(soup.find('p','story').previous) #returns empty or new-line. 
print(soup.find('p','title').next.next.next) #returns empty or newline similar to code above

print(soup.find('p','story').previous.previous)

print(soup.find('p','story').previous_element) #returns empty or new-line. 
print(soup.find('p','story').previous_element.previous_element)


print(soup.find('p','story').previous_element.previous_element.previous_element)

print(soup.find('p','title').next.next.previous.previous)

for element in soup.find('ul').next_elements:
    print(element)
	
print(soup.find('p','story').next)

print(soup.find('p','story').next_element)

print(soup.find('p','story').find_next()) #element after next_element

print(soup.find('p','story').find_next('h1'))

print(soup.find('p','story').find_all_next())

print(soup.find('p','story').find_all_next('li',limit=2))

print(soup.find('ul').previous.previous.previous)

print(soup.find('ul').find_previous())

print(soup.find('ul').find_previous('p','title'))

print(soup.find('ul').find_all_previous('p'))

print(soup.find('p','title').next_sibling) #returns empty or new-line

print(soup.find('p','title').next_sibling.next_sibling) #print(soup.find('p','title').next_sibling.next)

print(soup.find('ul').previous_sibling) #returns empty or new-line

print(soup.find('ul').previous_sibling.previous_sibling)

#using List Comprehension 
title = [ele.name for ele in soup.find('p','title').next_siblings]
print(list(filter(None,title)))

ul = [ele.name for ele in soup.find('ul').previous_siblings]
print(list(filter(None,ul)))

#find next <p> siblings for selected <p> with class=title
print(soup.find('p','title').find_next_siblings('p'))

#find single or next sibling for selected <h1>
print(soup.find('h1').find_next_sibling())

#find single or next sibling <li> for selected <h1>
print(soup.find('h1').find_next_sibling('li'))

#find first previous sibling to <ul>
print(soup.find('ul').find_previous_sibling())

#find all previous siblings to <ul>
print(soup.find('ul').find_previous_siblings())

#Using CSS Selectors - Skip this part
print(soup.select('li[data-id]'))
print(soup.select('ul li[data-id]')[1]) #fetch index 1 only from resulted List
print(soup.select_one('li[data-id]'))
print(soup.select('p.story > a.sister'))#Selects all <a> with class='sister' that are direct child to <p> with class="story"

print(soup.select('p b'))#Selects <b> inside <p>

print(soup.select('p + h1'))#Selects immediate <h1> after <p>

print(soup.select('p.story + h1'))#Selects immediate <h1> after <p> with class 'story'

print(soup.select('p.title + h1'))#Selects immediate <h1> after <p> with class 'title'

print(soup.select('a[href*="example.com"]'))

print(soup.select('a[id*="link"]'))