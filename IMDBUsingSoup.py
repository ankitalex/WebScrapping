from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = 'https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc&ref_=adv_prv'

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"lister-item-content"})
container=containers[0]
#print(soup.prettify(container))

for container1 in containers:
    movie_Names=page_soup.find_all('h3', {"class":"lister-item-header"})

    for movie_Name in movie_Names:
        if movie_Name.find('a'):
            print(movie_Name.find('a').text)
        print(movie_Name.find('span', {"class":"lister-item-year"}).text)
        movie_duration = page_soup.find_all('p', {"class": "text-muted"})  # .find('span', {"class": "runtime"}).text
        print(movie_duration[0].find('span', {"class": "runtime"}).text)
    #if movie_duration.find('span'):
    #    print(movie_duration.find_all('span', {"class": "runtime"}).text)
        #print(movie_Name.findAll('div', {"class": "ratings-bar"}).findAll('div', {"name": "ir"}).text)

