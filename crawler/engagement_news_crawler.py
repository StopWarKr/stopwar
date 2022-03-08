from textwrap import indent
from selenium import webdriver
import requests 
from bs4 import BeautifulSoup
import selenium
import json
import time
import os
import urllib.request
import urllib
from selenium.webdriver.common.keys import Keys
import base64
import re

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')

br = webdriver.Chrome("stopwar\crawler\chromedriver.exe", options=webdriver_options)
br.get("https://google.com")
time.sleep(3)
# iframe = br.find_element_by_xpath("//*[@id='backgroundImage']")
# br.switch_to.frame(iframe)
search_bar = br.find_element_by_name('q')
search_bar.send_keys("우크라이나 교전 상황")
search_bar.send_keys(Keys.ENTER)
time.sleep(3)

news_tag = br.find_element_by_xpath("//*[@id='hdtb-msb']/div[1]/div/div[4]/a")
news_tag.click()

json_data = []
news_index = 0
category = "engagement"
dataPath = "stopwar\crawlingData"
imgPath = "stopwar\crawlingData\img"

def download_image_from_url(name, img_data):
  name += " image.gif"
  name = re.sub("[V:*?\"<>|]", '', name)
  path = os.path.join(imgPath, name)
  with open(path, 'wb') as f:
    f.write(base64.decodebytes(base64.b64encode(bytes(img_data, 'utf-8'))))
  return path

def 기사크롤링(url):
  res = requests.get(url, headers = User_Agent_head)                                
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "html5lib")
  arr_news = soup.find_all("g-card", attrs = {"class" : "ftSUBd"})                  
                          
  for news in arr_news:
    news_index = 0

    name = news.find("div", attrs = {"class" : "mCBkyc y355M JQe2Ld nDgy9d"}).get_text()
    description = news.find("div", attrs = {"class" : "GI74Re nDgy9d"}).get_text()
    date = news.find_all("span")[2].get_text()
    news_link = news.find("a", attrs = {"class" : "WlydOe"})["href"]
    
    image = news.find("img", attrs={"class" : "rISBZc zr758c M4dUYb"})
    print(image)
    src = image['src']
    print(src)
    #image_link = download_image_from_url(name, src)
    
    print(str(news_index)+"번째 기사" '\n' , name, '\n', news_link)

    json_data.append({
      "name" : name, 
      "description" : description,
      "date" : date,
      "news_link" : news_link,
      #"image_link" : image_link,
      "category" : category
      })

    print("-" * 100, '\n')
    news_index += 1

기사크롤링(br.current_url)

import json

def create_json(language):
  language += "_"
  name = language + category + "NewsData.json"
  path = os.path.join("stopwar\crawlingData", name)
  with open(path, 'w', encoding="UTF-8-sig") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

create_json("kr")