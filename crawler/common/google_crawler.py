import requests
from bs4 import BeautifulSoup
import json

User_Agent_head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


class GoogleCrawler:
    def __init__(self, category):
        self.category = category
        self.news_list = []

    def __request_items(self, url):
        res = requests.get(url, headers=User_Agent_head)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.find_all('g-card', attrs={'class': 'ftSUBd'})

    def crawl_news(self, query, page):
        news_list = []
        for i in range(0, page):
            url = f'https://www.google.com/search?q={query}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={i * 10}'
            result = self.__request_items(url)  # todo: item 전부 다 잘 들어오는지 확인 필요
            for news in result:
                news_list.append(self.__parse_item(news))

        self.news_list = news_list
        return self

    def __get_image_url(self, url):
      newsResponse = requests.get(url)

      newsResponse.encoding = 'utf-8'
      newsHtml = newsResponse.text

      soup = BeautifulSoup(newsHtml, 'html.parser')

      if (soup.select_one('meta[property="og:image"]') == None):
        return 'No Image'

      image = soup.select_one('meta[property="og:image"]')['content']
      return image
      
      

    def __parse_item(self, news):
        title = news.find(
            'div', attrs={'class': 'mCBkyc y355M JQe2Ld nDgy9d'}).get_text()
        url = news.find('a', {'class': 'WlydOe'})['href']
        
        content = news.find(
            'div', attrs={'class': 'GI74Re nDgy9d'}).get_text()
        date = news.find(
            'div', attrs={'class': 'OSrXXb ZE0LJd'}).find('span').get_text()
        image = self.__get_image_url(url)

        return {
            'name': title,
            'description': content,
            'link': url,
            'date': date,
            'image_path': image,
            'catagory': self.category,
        }

    def write_json(self, filename):
        with open(f'./crawlingData/{filename}.json', 'w', encoding='UTF-8-sig') as f_write:
            json.dump(self.news_list, f_write, ensure_ascii=False, indent=4)
