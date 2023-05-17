import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


def analyzer_menu():
    print(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""
    )
    answer = input("Digite a opção desejada: ")
    if answer == "0":
        value = input("Digite quantas notícias serão buscadas: ")
        return get_tech_news(int(value))
    if answer == "1":
        value = input("Digite o título: ")
        return print(search_by_title(value))
    if answer == "2":
        value = input("Digite a data no formato aaaa-mm-dd: ")
        return print(search_by_date(value))
    if answer == "3":
        value = input("Digite a categoria: ")
        return print(search_by_category(value))
    if answer == "4":
        return print(top_5_categories())
    if answer == "5":
        return print("Encerrando script")
    else:
        print("Opção inválida", file=sys.stderr)
