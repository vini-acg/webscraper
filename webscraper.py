import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Scraper:

    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = requests.get(self.site)
        html = response.text
        parser = "html.parser"
        links = set()
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            href = tag.get("href")
            if href:
                full_url = urljoin(self.site, href)
                if full_url not in links:
                    links.add(full_url)
                    print(full_url)


scrape = Scraper('https://news.google.com/')
scrape.scrape()
