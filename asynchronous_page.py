import pandas
import json
import requests
from bs4 import BeautifulSoup
import pandas
import re
import os
import sys

def request_link(link):
    headers = { 
        'accept': 'application/json', 
    }
    res = ""

    try:
        res = requests.get(link, headers=headers)
    except requests.exceptions.RequestException as e:
        print(res)
        res = "error"

    return res

def parse_page(link):
    
    res = request_link(link=link)
    content = res.json()
    colTitle = []

    for elem in content["data"]:
        colTitle.append(elem["name"])

    df = pandas.DataFrame({"title": colTitle})
    df.to_csv("titles_program.csv")

parse_page(link = "https://api.mygermanuniversity.com/api/study-programs?page=1&per_page=25&sorting=featured&direction=ASC&add_to_history=true&degree_level_id=1&short_info=true&clientCountry=FR")

