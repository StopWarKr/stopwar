import requests
import re
from bs4 import BeautifulSoup
import json

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
english_result = []
korean_result = []

def createJs(title, result): # json 파일로 변경
  with open('{}.json'.format('./crawlingData/' + title), 'w', encoding = "UTF-8-sig") as f_write:
    json.dump(result, f_write, ensure_ascii = False, indent = 4)

  data = ""
  with open('{}.json'.format('./crawlingData/' + title), "r", encoding = "UTF-8-sig") as f:
    line = f.readline()
    while line:
      data += line
      line = f.readline()


def google_sponser(search, page, file_name, category):
    start = 0
    for i in range(1, page + 1):
        url = 'https://www.google.com/search?q={}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={}&sa=N&ved=2ahUKEwipvcTD6rP2AhVcyosBHZ4cDaQ4KBDy0wN6BAgBED8&biw=1920&bih=937&dpr=1'.format(search, start)
        res = requests.get(url, headers = User_Agent_head)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("g-card", attrs = {"class" : "ftSUBd"})
        start += 10

        for i in range(len(news)):
            title = news[i].find("div", attrs = {"class" : "mCBkyc y355M JQe2Ld nDgy9d"}).get_text()
            link = news[i].find("a", {"class" : "WlydOe"})["href"]
            if search == 'Ukraine Sponsor':
                english_result.append({'제목': title, '링크': link, '카테고리': category})
            else:
                korean_result.append({'제목': title, '링크': link, '카테고리': category})
        if search == 'Ukraine Sponsor':
            createJs(file_name, english_result)
        else:
            createJs(file_name, korean_result)

# English
google_sponser('Ukraine Sponsor', 3, 'en_SponserNewsData', '후원')

# Korean
google_sponser('우크라이나 후원', 3, 'kr_SponserNewsData', '후원')
