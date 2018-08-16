# Craigslist-Finder

Digs thourgh the Html of craigslist searches to find you posts that match your search and descriptions of individual posts.  Can be used with twilio to send you text meassages with information on new posts matching a search

## Getting Started

you can pip install from this github page or download the crcrawler.py file directly. If you download it directly, place it in your folder you're working on and import it like you would with any module. 

### Prerequisites

Python 3

Beautifulsoup

```
https://www.python.org/downloads/
pip install bs4
```

to use with twilio check out the twilio documentation on how to send yourself texts with python

'''
https://www.twilio.com/docs/sms/quickstart/python
'''



### Methods



```
crcrawler.getposts(URL)
```

Parameters: url link of craigslist search (string)

Returns: list of strings (Urls of craigslist posts of given search)


```
crcrawler.getinfo(URL)
```

Parameters: url link of craigslist post(string)

Returns:(string) information about post in the form (price,title,description)


## Example Tutorials

Example 1: printing information from craigslist search posts

```
import clcrawler as cc

searchpage="https//craigslist....."       #whatever craigslist page you're interested in

posts=cc.getposts(searchpage)

for post in posts:
       print(cc.getinfo(post))

#this prints the price,title and description of each post on that page
```

Example 2: sending updates to a phone (with twilio)
```
import clcrawler as cc
import time

searchpage="https//craigslist..."         #whatever craigslist page you're interested in
posts=cc.getposts(searchpage)

#make sure you have a way to exit the program, this is an infinite loop

while True:
       listings=[]
       newposts=cc.getposts(searchpage)
       for newpost in newposts:
              if newpost not in posts:
                     listings.append(newpost)
       for list in listing:
              message=cc.getinfo(list)
              twilio.sendmessage(message,"33355432314")   #look above for the link about twilio documentation
       posts=newposts
       
       time.sleep(1800)  #let the program sleep for 30 minutes so 30 minutes later it can check for new posts.  
```

*editors notes on Example 2:
**For the link that is pagesearch, Use as many filters as you can. To broad of a search can blow up your phone especially while looking for cars.  Car dealerships use lots of keywords to make their "advertisments" pop up in many different search filters.



## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
       



