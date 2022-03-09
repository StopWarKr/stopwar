import requests
import re
from bs4 import BeautifulSoup
import json

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
english_result = []

# WORLD HISTORY ENCYCLOPEDIA에서 ukraine를 검색한 결과를 크롤링하였습니다.

def createJs(title, result): # json 파일로 변경
  with open('{}.json'.format(title), 'w', encoding = "UTF-8-sig") as f_write:
    json.dump(result, f_write, ensure_ascii = False, indent = 4)

  data = ""
  with open('{}.json'.format(title), "r", encoding = "UTF-8-sig") as f:
    line = f.readline()
    while line:
      data += line
      line = f.readline()


def ukraineHistory_en(search, page, file_name, category):
    # start = 1은 1page 2는 1page
    start = 1
    for i in range(1, page+1):
        url = 'https://www.worldhistory.org/search/?q={}&page={}'.format(search,start)
        res = requests.get(url, headers = User_Agent_head)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        history = soup.find_all("a", "content_item")

        # 1page 마다 10개의 개시글이 있음
        for j in range(10):
          title = history[j].find("h3").get_text()
          link = "https://www.worldhistory.org" +history[j]["href"]
          english_result.append({"title":title,"link":link, "category":category})
        
        start += 1

        
        createJs(file_name, english_result)


# English
ukraineHistory_en("ukraine", 2, "English_UkraineHistory", "history")
print(english_result)
