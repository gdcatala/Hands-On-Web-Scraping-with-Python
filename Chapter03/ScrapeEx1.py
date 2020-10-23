import lxml.html

###################################LXML LIBRARY########################################################
#The basic structure of the lxml library is the "Element" object that represent a node in the node tree.
#Every thing is node: (i) The entire document is a document node, (ii) Every HTML/XML element is an element
#node, and (iii) The text inside HTML/XML elements are text nodes.

#The Element's type can be described as a cross between a list and a dic. To make the access to these
#subelements easy and straight forward,  Element mimic the behaviour of normal Python lists as closely
#as possible. For example child1 = root[0], child2 = root[1] and so on. An element's length is its number
#of subelements.


#In the following code a URL (musicURL) is parsed using the .parse() function, which results in
#the "doc" object (class: lxml.etree.ElementTree)

musicUrl= "http://books.toscrape.com/catalogue/category/books/music_14/index.html"

#The .parse() method returns an etree object. Using the .getroot() method we obtain the root Element of
#etree

doc = lxml.html.parse(musicUrl).getroot()

#In this snippet we create a text file called "BooktoScrape" with the whole content of the parsed webpage

string_booktoscrape = lxml.html.tostring(doc, method='html')
with open("BooktoScrape.txt", "wb") as file:
    file.write(string_booktoscrape)

#With the .iter() method we can loop over the Element and all subelements in document order,
#returning all elements with a matching tag. By default tag = None, so returns all the subelements

########################################XPATH EXPRESSIONS################################################
#XPath uses path expressions to select nodes or node-sets in an XML/HTML document. The most usefull
#expressions are:

#(i) nodename->Selects all nodes with the name "nodename",
#(ii) /->Selects from the root node
#(iii) //->Selects nodes in the document from the current node that match the selection no matter where
#they are
#(iv) @->Selects attributes
#(v)/bookstore/book[1]-> Selects the first book element that is the child of the bookstore element
#(vi) //title[@lang='en']->Selects all the title elements that have a "lang" attribute with a value of "en"


Book_Title = doc.xpath("/html/body/div/div/div/div/section/div[2]/ol/li[1]/article[1]/h3/a/text()")
print(f"Book Title: {str(Book_Title[0])}")

#################################.XPATH METHOD####################################################
#The .xpath() method returns a list containing every Element that matches with the XPath expresion.
#.path("XPath expression")[0] returns the first Element that matches the expression
#.xpath("XPath expression")[0][0] returns the first child of the first Element


#The articles object is a list containing all article Elements inside the li[1]. The article object
#represent the first object of the former list.
articles = doc.xpath("//*[@id='default']/div/div/div/div/section/div[2]/ol/li[1]/article[1]/h3")
article = articles[0]

#individual element inside base
title = articles[0].xpath("//h3/a/text()")
title2 = doc.xpath("//h3/a/text()")

price = article.xpath("//div[2]/p[contains(@class,'price_color')]/text()")
price2 = doc.xpath("//div[2]/p[contains(@class,'price_color')]/text()")

availability = article.xpath("//div[2]/p[2][contains(@class,'availability')]/text()[normalize-space()]")
availability2 = doc.xpath("//div[2]/p[2][contains(@class,'availability')]/text()[normalize-space()]")

imageUrl = article.xpath("//div[1][contains(@class,'image_container')]/a/img/@src")
imageUrl2 = doc.xpath("//div[1][contains(@class,'image_container')]/a/img/@src")

starRating = article.xpath("//p[contains(@class,'star-rating')]/@class")
starRating2 = article.xpath("//p[contains(@class,'star-rating')]/@class")

#cleaning and formatting 
stock = list(map(lambda stock:stock.strip(),availability))
images = list(map(lambda img:img.replace('../../../..','http://books.toscrape.com'),imageUrl))
rating = list(map(lambda rating:rating.replace('star-rating ',''),starRating))

print(title)
print(price)
print(stock)
print(images)
print(rating)

#The .zip() function collects individual indexes from all provided list objects and appends them as a
#tuple
dataset = zip(title,price,stock,images,rating)
print(list(dataset))
