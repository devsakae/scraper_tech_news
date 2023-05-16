import requests
import time
from parsel import Selector


headers = {'user-agent': 'Fake user-agent'}


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str) -> list[dict]:
    selector = Selector(html_content)
    links = []
    for link in selector.css('h2.entry-title a::attr(href)').getall():
        links.append(link)
    return links


# Requisito 3
def scrape_next_page_link(html_content: str) -> str | None:
    selector = Selector(html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
