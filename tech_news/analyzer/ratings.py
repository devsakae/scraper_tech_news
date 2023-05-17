from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    data = find_news()
    categories = Counter([n["category"] for n in data]).most_common(5)
    categories.sort(key=lambda x: x[0])
    categories.sort(key=lambda x: x[1], reverse=True)
    return [c[0] for c in categories]
