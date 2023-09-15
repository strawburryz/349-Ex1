# Script to determine number of unique CSS properties used on a website's external stylesheets
# Example: py css_scrape.py https://adrxone.github.io/Exercise-1

from bs4 import BeautifulSoup
import requests
import sys
import cssutils
import logging

cssutils.log.setLevel(logging.CRITICAL)
sheets = set()
hrefs = ["/","index.html"]
elements = set()

def scrape(site, path):
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(site + path).text
    print(site + path)

    # Parse the html content using any parser
    s = BeautifulSoup(html_content, "html.parser")

    # Get all the external stylesheet links
    for link in s.findAll("link"):
        if 'href' in  link.attrs:
            href = link.attrs['href']
            href = "/" + href if not href.startswith("/") else href
            sheets.add(site + href)
            
    # Recurse to get all the anchors
    for i in s.find_all("a"):
        if ('href' in i.attrs):
            href = i.attrs['href']
            if not href.startswith(("https", "http", "www")):
                href = "/" + href if not href.startswith("/") else href
                if href not in hrefs:
                    hrefs.append(href)
                    scrape(site, href)


def parse():
    bucket = set()
    for sheet in sheets:
        style = cssutils.parseUrl(sheet)
        for rule in style:
            if rule.type == rule.STYLE_RULE:
                for property in rule.style:
                    bucket.add(property.name)

    print(sorted(bucket))
    print(f'Number of Unique CSS Properties is {len(bucket)}')



if __name__ == "__main__":
    site = sys.argv[1]
    scrape(site, "")
    print(sheets)
    parse()

