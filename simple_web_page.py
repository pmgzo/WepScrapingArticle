import pandas
import json
import requests
from bs4 import BeautifulSoup
import pandas
import re
import os
import sys

def request_link(link):
    headers = { 'accept': 'text/html'}
    res = ""

    try:
        res = requests.get(link, headers=headers)
    except requests.exceptions.RequestException as e:
        res = "error"

    return res

def parse_page(link):
    res = request_link(link=link)
    content = res.content.decode("utf-8")
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.select("span.titleline > a")

    colTitle = []

    for article in articles:
        print(article.get_text())
        colTitle.append(article.get_text())

    df = pandas.DataFrame({"title": colTitle})
    df.to_csv("hacker_news_title.csv")

parse_page(link="https://news.ycombinator.com/")