# flakes8: noqa E501
from tech_news.database import find_news
from datetime import datetime
from tech_news.color import color


def search_by_title(title):
    data = find_news()
    response = []
    for new in data:
        if title.lower() in new["title"].lower():
            resume = (
                f"""\n{color.BLUELINE}Título{color.END}: {new["title"]}
{color.BLUELINE}Sumário{color.END}: {new["summary"]}
{color.BLUELINE}URL{color.END}: {new["url"]}"""
                    )
            response.append(resume)
    return response


def search_by_date(date):
    try:
        newdate = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        data = find_news()
        response = []
        for new in data:
            if newdate in new["timestamp"]:
                resume = (
                    f"""\n{color.BLUELINE}Título{color.END}: {new["title"]}
{color.BLUELINE}Publicada em{color.END}: {new["timestamp"]}
{color.BLUELINE}URL{color.END}: {new["url"]}"""
                        )
                response.append(resume)
        return response
    except ValueError:
        raise ValueError("Data inválida")


def search_by_category(category):
    data = find_news()
    response = []
    for new in data:
        if category.lower() in new["category"].lower():
            resume = (
                f"""\n{color.BLUELINE}Título{color.END}: {new["title"]}
{color.BLUELINE}URL{color.END}: {new["url"]}"""
                    )
            response.append(resume)
    return response
