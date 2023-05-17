from tech_news.database import find_news
from datetime import datetime


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
    try:
        newdate = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        data = find_news()
        response = []
        for new in data:
            if newdate in new["timestamp"]:
                response.append((new["title"], new["url"]))
        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
