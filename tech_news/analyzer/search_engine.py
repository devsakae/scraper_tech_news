from tech_news.database import find_news
from datetime import datetime


def search_by_title(title):
    data = find_news()
    response = []
    for new in data:
        if title.lower() in new["title"].lower():
            response.append((new["title"], new["url"]))
    return response


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


def search_by_category(category):
    data = find_news()
    response = []
    for new in data:
        if category.lower() in new["category"].lower():
            response.append((new["title"], new["url"]))
    return response
