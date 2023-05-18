# flake8: noqa
import sys
import time
from tech_news.color import color
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    get_all_news,
    search_by_title,
    search_by_date,
    search_by_category,
)

def printnews(data):
    if len(data) == 0:
        print(f"\n*** {color.PURPLE}Aviso{color.END}: Nenhuma notícia encontrada")
    else:
        for new in data:
            print(new)

def analyzer_menu():
    print(
        f"""\n{color.BOLDBLUE}Python scraper by @devsakae{color.END}\n
 {color.GREY}Digite {color.END}1{color.GREY} para atualizar o banco de dados
 Digite {color.END}2{color.GREY} para ler todas as manchetes
 Digite {color.END}3{color.GREY} para pesquisar notícias por TÍTULO
 Digite {color.END}4{color.GREY} para pesquisar notícias por DATA
 Digite {color.END}5{color.GREY} para pesquisar notícias por CATEGORIA\n
Ou digite {color.END}q{color.GREY} para {color.END}{color.RED}finalizar{color.END}{color.GREY} o script.{color.END}\n"""
    )
    answer = input(">> Digite a opção desejada: ")
    if answer == "1":
        value = input("Digite quantas notícias serão buscadas: ")
        get_tech_news(int(value))
    elif answer == "2":
        printnews(get_all_news())
    elif answer == "3":
        printnews(search_by_title(input("Pesquisar por qual string? ")))
    elif answer == "4":
        printnews(search_by_date(input("Digite a data a pesquisar (formato aaaa-mm-dd): ")))
    elif answer == "5":
        print(top_5_categories())
        printnews(search_by_category(input("Escreva qual categoria deseja ler: ")))
    elif answer == "q":
        return print(f"\n{color.BOLDRED}*** Encerrando script ***{color.END}\n")
    else:
        print(f"\n*** {color.BOLDRED}Erro{color.END}: Opção inválida", file=sys.stderr)
    time.sleep(1)
    analyzer_menu()
