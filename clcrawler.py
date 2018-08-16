#craiglist crawler
# contains methods for scrapping craigslist
# as a hint, use ==python -m pip install SomePackage== to install pkg

from bs4 import BeautifulSoup
import requests

def getposts(link):
    page = requests.get(link)

    #print(page.status_code)#if code is 200 page is ok if not page is bad

    soup = BeautifulSoup(page.content, 'html.parser')

    posts=[]####will be a list of tags

    links=[]

    posts=soup.find_all("a",class_="result-title hdrlnk")

    for post in posts:
        links.append(post.get("href"))

    return links


def getinfo(link):
    page = requests.get(link)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title=str(soup.find("title"))
    dash=title.find('-')
    if dash != -1:
        title=title[7:dash]
    
    cost=None   
    price=soup.find("span",class_="price")
    #print(type(price))
    if price is None:
        cost=" no cost listed "
    else:
        cost=price.get_text()
    

    meta=soup.find_all("meta")
    descr=None
    for tag in meta:
        if tag.get("name")=="description":
            descr=tag.get("content")
        
        
    
    
    
    return cost,title,descr



    



    



