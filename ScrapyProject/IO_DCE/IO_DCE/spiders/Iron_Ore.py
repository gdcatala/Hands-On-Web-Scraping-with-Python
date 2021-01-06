import scrapy
import re

class IronOreSpider(scrapy.Spider):
    #This is the name of the Spider
    name = 'Iron_Ore'
    allowed_domains = ['www.dce.com.cn/webquote/futures_quote_en.jsp?varietyid=I']
    #The start_urls class attribute contains a list of URLs. Returns an iterable of
    #Request objects which the Spider will begin crawling from.
    start_urls = ['http://www.dce.com.cn/webquote/futures_quote_en.jsp?varietyid=I']

    def parse(self, response):
    #A method that will be called to handle the response downloaded for each of
    #the requests made. The response parameter is an instance of TextResponse that
    #holds the page content and has further helpful methods to handle it.

        current_date = re.sub('[\D]', '', response.xpath('//p/text()').get())

        prices = []

        for i in response.xpath('//table[@id="dataT"]/tr'):
            prices.append(i.xpath('.//td[15]/text()').extract_first())

        with open("data.txt", "w") as file:
            file.write(str(current_date))
            file.write("\n")
            file.write(str(prices))

        yield {current_date: prices}

        self.log("Saved file data.txt")
