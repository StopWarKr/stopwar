import requests
from bs4 import BeautifulSoup
import json

User_Agent_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}


def crawl_items(url):
    res = requests.get(url, headers=User_Agent_head)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find_all("g-card", attrs={"class": "ftSUBd"})


def parse_item(news, category):
    title = news.find(
        "div", attrs={"class": "mCBkyc y355M JQe2Ld nDgy9d"}).get_text()
    url = news.find("a", {"class": "WlydOe"})["href"]
    source = news.find(
        'div', attrs={"class": "CEMjEf NUnG9d"}).find('span').get_text()
    content = news.find(
        "div", attrs={"class": "GI74Re nDgy9d"}).get_text()

    return {
        'title': title,
        'link': url,
        'catagory': category,
        'source': source,
        'content': content,
        # todo: date 추가 필요
    }


def process_crawling(search_param, page, file_name, category):
    pages = crawl_pages(search_param, page, category)
    create_js(file_name, pages)


def crawl_pages(search_param, page, category):
    newsList = []
    for i in range(0, page):
        url = f'https://www.google.com/search?q={search_param}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={i * 10}'
        result = crawl_items(url)  # todo: item 전부 다 잘 들어오는지 확인 필요
        for news in result:
            newsList.append(parse_item(news, category))
    return newsList


def create_js(title, datas):
    with open(f'./crawlingData/{title}.json', 'w', encoding="UTF-8-sig") as f_write:
        json.dump(datas, f_write, ensure_ascii=False, indent=4)


process_crawling('ukraine regulation', 3, 'en_RegulationNewsData', '규제')
process_crawling('우크라이나 규제', 3, 'kr_RegulationNewsData', '규제')
