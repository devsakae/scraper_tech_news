# flake8: noqa
import requests
import time
from parsel import Selector
from tech_news.database import create_news
from tech_news.color import color
from tqdm import tqdm


headers = {"user-agent": "Fake user-agent"}


def fetch(url):
    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


def scrape_updates(html_content: str) -> list[dict]:
    selector = Selector(html_content)
    links = []
    for link in selector.css("h2.entry-title a::attr(href)").getall():
        links.append(link)
    return links


def scrape_next_page_link(html_content: str) -> str | None:
    selector = Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


def scrape_news(html_content: str) -> list[dict]:
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("div.entry-header-inner.cs-bg-dark > h1::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("h5.title-author > span > a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    summary = selector.css("div.entry-content > p").xpath("string()").get()
    category = selector.css("span.label::text").get()
    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": str(writer).strip(),
        "reading_time": int(reading_time.split(" ")[0]),
        "summary": summary.strip(),
        "category": category,
    }


def get_tech_news(amount: int) -> list[dict]:
    pages = amount / 12
    html = fetch("https://blog.betrybe.com/")
    links = scrape_updates(html)
    while pages > 1:
        html = fetch(scrape_next_page_link(html))
        newpagelinks = scrape_updates(html)
        links += newpagelinks
        pages -= 1
    alllinks = iter(links)
    news = []
    for _ in tqdm(range(amount),
            desc="Carregando…",
            ascii=False,
            ncols=75):
        scrapped = fetch(next(alllinks))
        formatted = scrape_news(scrapped)
        news.append(formatted)
    create_news(news)
    print(f"{color.GREEN}Finished{color.END}{color.GREY}:{color.END}{color.BOLD} {amount} {color.END}{color.GREY}notícias adicionadas ao seu banco de dados{color.END}")
