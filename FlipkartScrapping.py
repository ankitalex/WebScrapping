### Flipkart HTML Parsing
### https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"_2kHMtA"})
container=containers[0]
#print(len(containers))
#print(soup.prettify(container))
#Name=container.findAll("div", {"class":"_4rR01T"})
#print(Name[0].text)
print("*"*20,'Flipkart product details',"*"*20)
for container in containers:
    product_name=container.findAll("div", {"class": "_4rR01T"})
    print(product_name[0].text)
    print("*" * 50)
    product_original_price = container.findAll("div", {"class": "_3I9_wc _27UcVY"})
    print(product_original_price[0].text)
    product_discount = container.findAll("div", {"class": "_3Ay6Sb"})
    print(product_discount[0].text)
    product_final_price = container.findAll("div", {"class": "_30jeq3 _1_WHN1"})
    print(product_final_price[0].text)
    product_Rating = container.findAll("div", {"class": "_3LWZlK"})
    print(product_Rating[0].text)
    product_reviews = container.findAll("span", {"class": "_2_R_DZ"})
    print(product_reviews[0].text)
    print("*" * 50)
