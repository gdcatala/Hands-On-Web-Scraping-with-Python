#The following links are some XPath and CSS selectors collected using DevTools
#for items available with products such as book title and price

#The XPath expressions navigate hierarchically through elements and reach the
#targeted one. XPath expressions works in the same way as the Linux file system
#where individual elements are identified with their position and represented by
#an index number

xpath_title = "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a"
xpath_price = "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]"
xpath_image = "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/div[1]"
xpath_stock_information = "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[2]"
xpath_star_rating = "/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/p"

#CSS selectors are defined patterns used to select HTML elements, using the element
#name or global attributes. The "p.header" selects <p> with class=header and the
#"p#link" selects <p> elements with id=link. The "p > a" selects all <a> elements
#that are a direct child of <div>. That is why CSS is less intuitive that XPath

css_title = "li.col-xs-6:nth-child(1) > article:nth-child(1) > h3:nth-child(3) > a:nth-child(1)"
css_price = "li.col-xs-6:nth-child(1) > article:nth-child(1) > div:nth-child(4) > p:nth-child(1)"