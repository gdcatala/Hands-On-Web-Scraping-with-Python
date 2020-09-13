#lxml is a XML toolkit, with a rich library set to process XML
#and HTML. lxml is preferred over other libraries for its high
#speed and effective memory management.

#Elements of a markup language such as XML and HTML have start
#and close tags; tags can also have attributes and contain other
#elements

#The lxml library contains important modules; (i) lxml.etree: parsing
#and implementing ElementTree, supports XPath, iterations and more
#(ii)lxml.html: parses HTML and (iii) lxmlcssselect: convert CSS
#selectors into XPath expressions


#In this example we will be reading the XML file content available from
#the food.xml file.

from lxml import etree

#The XML file is read in binary format

xml = open("food.xml","rb").read()

#The XML response obtained from the preceding code needs to be parsed
#and traversed using lxml.etree.XML(), method that parses the XML
#document and returns the menu root node (in this case)

tree = etree.XML(xml)

#The etree.parse method is used to solve encoding/decoding the file's
#contenta and is really an effective approach for reading content from
# a file, HTTP URL or FTP

print(tree)
print(type(tree))

#Tree iteration is performed using the iter() function. The elements'
#tag name can be accessed using the element property "tag", similarly,
#elements' text can be accessed by the text property

for element in tree.iter():
    print("%s - %s" % (element.tag, element.text))

#We can pass child elements as an argument to the tree iterator (price
# and name) to obtain selected element-based responses
for element in tree.iter('price','name'):
    print("%s - %s" % (element.tag, element.text))

#iter through description
for element in tree.iter('description'):
    print("%s - %s" % (element.tag, element.text))

