import requests
from bs4 import BeautifulSoup
from config import DEFAULT_HEADERS

class PageLoader():

    def get_page(self, url):
        
        r = requests.get(url=url, headers=DEFAULT_HEADERS)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        return soup
        