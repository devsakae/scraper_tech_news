import requests

headers = {'user-agent': 'Fake user-agent'}


# Requisito 1
def fetch(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)


fetch('https://blog.betrybe.com/')


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
