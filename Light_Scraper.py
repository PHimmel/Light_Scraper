"""
create a basic scraper
for what?
what interests me:
rpi

10 degrees of separation from wiki

input:
1) topic name
2) proximity of random link (first sentence, paragraph, whole page)

output:
1) final wiki page
2) all links in the chain to final wiki page

design to be utilized through React, send request to pi flask server


"""
from bs4 import SoupStrainer as Ss
import urllib
from urllib import request


class Scraper(object):

    def __init__(self, search):
        self.search = search
        self.html = None
        self.soup = None

    def __repr__(self):
        return 'Scraper:{}'.format(self.search)

    def get_html(self):
        try:
            self.html = urllib.request.urlopen(self.search).read()
        except ValueError:
            exit(1)

    def make_soup(self):
        self.soup = Ss(self.html, 'html.parser')


taco = Scraper('https://en.wikipedia.org/wiki/Taco')
taco.get_html()
taco.make_soup()
print(taco.soup)