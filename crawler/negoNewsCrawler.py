import requests 
from bs4 import BeautifulSoup
import json

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}


def process_crawling(search_param, page, file_name, category):
    pages = crawling_pages(search_param, page)
    datas = crawling_news(pages, category)
    create_js(file_name, datas)

def crawling_pages(search_param, page):
    start = 0
    newsList = []
    for i in range(1, page+1):
        # start = 0은 1page 10은 2page 20은 3page
        url = f'https://www.google.com/search?q={search_param}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={start}&sa=N&ved=2ahUKEwipvcTD6rP2AhVcyosBHZ4cDaQ4KBDy0wN6BAgBED8&biw=1920&bih=937&dpr=1'
        res = requests.get(url, headers = User_Agent_head)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("g-card", attrs = {"class" : "ftSUBd"})
        start += 10
        newsList.append(news)
    return newsList

def crawling_news(pages, category):
    datas = []
    for news_per_page in pages:
        for news in news_per_page:
            title = news.find("div", attrs = {"class" : "mCBkyc y355M JQe2Ld nDgy9d"}).get_text()
            url = news.find("a", {"class" : "WlydOe"})["href"]
            datas.append({'title': title, 'link' : url, 'catagory': category} )
    return datas

def create_js(title, datas): 
  with open(f'./crawlingData/{title}.json', 'w', encoding = "UTF-8-sig") as f_write:
    json.dump(datas, f_write, ensure_ascii = False, indent = 4)

# Todo
# url = (
#     f'https://www.google.com/search?q={search_param}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={start}&sa=N&ved=2ahUKEwipvcTD6rP2AhVcyosBHZ4cDaQ4KBDy0wN6BAgBED8&biw=1920&bih=937&dpr=1'
#     , 'bbc'
#     , 'zdf'
#     , 'kbs'
#     , 'nhk'
# )
process_crawling('ukraine negotiation progress situation', 3, 'en_NegoNewsData','협상 진행 과정')
process_crawling('우크라이나 협상 진행 상황', 3, 'kr_NegoNewsData', '협상 진행 과정')
