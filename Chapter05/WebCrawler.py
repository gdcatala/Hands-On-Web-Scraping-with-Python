###########################################BUILDING A WEB CRAWLER############################################

'''Listing Quotes from first 5 or less pages found from 'http://quotes.toscrape.com/'''

import requests
import re
from bs4 import BeautifulSoup
import csv

sourceUrl = 'http://quotes.toscrape.com/'

#"keys" is list object that contains the column's name that will be used while writing
#records to an external file

keys = ['quote_tags','author_url','author_name','born_date','born_location','quote_title']

#The read_url function will be used to make a request and recieve a response using the request library
#This function is supplied with a dynamically generated page URL to manage the pagination.

def read_url(url):
    """Read given Url , Returns requests object for page content"""
    response = requests.get(url)
    return response.text


def get_details(page, dataWriter):
    """Get 'response' for first 5 pages, parse it and collect data for 'keys' headers"""
    nextPage = True
    pageNo = 1
    while (nextPage and pageNo <= 5):
#The structure of the pagination is http://quotes.toscrape.com/page/1/ and so on

        response = read_url(page + 'page/' + str(pageNo))
        soup = BeautifulSoup(response, 'lxml')

#The rows obtained using the soup list all the quotes available in a single page found inside the
#<div class = "quote"> function and will be iterated to scrape data for individual items

        rows = soup.find_all('div', 'quote')

        if (len(rows) > 0):
            print("Page ",pageNo," Total Quotes Found ",len(rows))
            for row in rows:
                if row.find('span',attrs={'itemprop':'text'}):
                    title = row.find(attrs={'itemprop':'text'}).text.strip()
                    author = row.find(attrs={'itemprop':'author'}).text.strip()
                    authorLink = row.find('a',href=re.compile(r'/author/')).get('href')
                    tags = row.find('div','tags').find(itemprop="keywords").get('content')
                    print(title, ' : ', author,' : ',authorLink, ' : ',tags)

                    if authorLink:
                        authorLink = 'http://quotes.toscrape.com' + authorLink
                        linkDetail = read_url(authorLink)
                        soupInner = BeautifulSoup(linkDetail, 'lxml')

                        born_date = soupInner.find('span','author-born-date').text.strip()
                        born_location = soupInner.find('span','author-born-location').text.strip()

                        # Write a list of values in file
                        dataWriter.writerow([tags,authorLink,author,born_date,born_location.replace('in ',''),title])

            nextPage = True
            pageNo += 1
        else:
            print("Quotes Not Listed!")



if __name__ == '__main__':

#Dateset is defined to manage the external file quotes.csv. csv.writer() file is use for accessing CSV-based
#properties

    dataSet = open('quotes.csv', 'w', newline='', encoding='utf-8')
    dataWriter = csv.writer(dataSet)

#The .writerow() function is passed with keys for writing a row containing the column names from the list
#keys to the external file

    dataWriter.writerow(keys)

#The implemented get_details() function is being coded for pagination and scraping logic.

    get_details(sourceUrl, dataWriter)

    # get_details(sourceUrl)
    dataSet.close()
