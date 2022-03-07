import requests 
import re
from bs4 import BeautifulSoup
import csv
import json

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

L = []

def createJs(title): # json 파일로 변경
  with open('{}.json.'.format(title), 'w', encoding = "UTF-8-sig") as f_write:
    json.dump(L, f_write, ensure_ascii = False, indent = 4)

  data = ""
  with open('{}.json.'.format(title), "r", encoding = "UTF-8-sig") as f:
    line = f.readline()
    while line:
      data += line
      line = f.readline()


def 기사크롤링(검색, page, 파일이름):

    start = 0
    for i in range(1, page+1):
        # start = 0은 1page 10은 2page 20은 3page
        url = 'https://www.google.com/search?q={}&hl=ko&tbm=nws&ei=4eMlYunIJNyUr7wPnrm0oAo&start={}&sa=N&ved=2ahUKEwipvcTD6rP2AhVcyosBHZ4cDaQ4KBDy0wN6BAgBED8&biw=1920&bih=937&dpr=1'.format(검색, start)
        res = requests.get(url, headers = User_Agent_head)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.find_all("g-card", attrs = {"class" : "ftSUBd"})
        
        start += 10

        번수 = 1
        for 뉴스 in news:
            제목 = 뉴스.find("div", attrs = {"class" : "mCBkyc y355M JQe2Ld nDgy9d"}).get_text()
            링크 = 뉴스.find("a", {"class" : "WlydOe"})["href"]
            L.append({'제목': 제목, '링크' : 링크} )
            번수 += 1
    createJs(파일이름)
    

기사크롤링('ukraine damage situation', 3, 'English_UkraineDamageSituationNewsData')
L = []
기사크롤링('우크라이나 피해 상황', 3, 'Korean_UkraineDamageSituationNewsData')

print("Test")
