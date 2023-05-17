from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    data = find_news()
    response = []
    for new in data:
        if title.lower() in new["title"].lower():
            response.append((new["title"], new["url"]))
    return response


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
