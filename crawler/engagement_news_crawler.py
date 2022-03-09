from importlib.resources import path
from textwrap import indent
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
import time
import os
import urllib
from selenium.webdriver.common.keys import Keys
import base64
import re
from PIL import Image
from io import BytesIO
from selenium import webdriver
import json

# User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

# 이미지 다운로드 함수
imgPath = "crawlingData\img"
def download_image_from_src(name, img_data):
  name += " image.png"
  name = re.sub("[V:*?\"<>|]", '', name)
  path = os.path.join(imgPath, name)

  img_data = re.sub('^data:image/.+;base64,', '', img_data)
  img = Image.open(BytesIO(base64.b64decode(img_data)))
  img.save(path, "PNG")
  return path

# 폴더 안의 모든 파일 삭제 함수
def remove_all_file_in_forder(_path):
  if(os.path.exists(_path)):
    for file in os.scandir(_path):
      os.remove(file.path)

# 현재 페이지에서 뉴스 데이터 가져오기
def get_news_data_from_current_page(source):
  news_data = []
  news_index = 0
  #res = requests.get(url, headers = User_Agent_head)                             
  #res.raise_for_status()
  time.sleep(3)
  soup = BeautifulSoup(source, "html5lib")
  time.sleep(3)
  
  arr_news = soup.find_all("g-card", attrs = {"class" : "ftSUBd"})
  for news in arr_news:
    news_index += 1

    name = news.find("div", attrs = {"class" : "mCBkyc y355M JQe2Ld nDgy9d"}).get_text()
    description = news.find("div", attrs = {"class" : "GI74Re nDgy9d"}).get_text()
    date = news.find_all("span")[2].get_text()
    news_link = news.find("a", attrs = {"class" : "WlydOe"})["href"]
    
    src = news.find("img", attrs={"class" : "rISBZc zr758c M4dUYb"})['src']
    image_path = download_image_from_src(name, src)

    print(str(news_index)+"번째 기사" '\n' , name, '\n', news_link)

    news_data.append({
      "name" : name, 
      "description" : description,
      "date" : date,
      "news_link" : news_link,
      "image_path" : image_path,
      "category" : category
      })

    print("-" * 100, '\n')
    
  return news_data


# json파일 생성하는 함수
category = "engagement"
jsondata_path = "crawlingData"
def create_json(language, json_data):
  language += "_"
  name = language + category + "NewsData.json" # 이름은 양식이 정해져 있으므로 따로 인자값을 받지 않음
  path = os.path.join(jsondata_path, name)
  with open(path, 'w', encoding="UTF-8-sig") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)



# dirver 세팅
webdriver_options = webdriver.ChromeOptions()
#webdriver_options.add_argument('headless')
#webdriver_options.add_argument("window-size=800x600") # 안보이는 창의 크기를 몇으로 할건지 정의
time.sleep(1)
driver = webdriver.Chrome("crawler\chromedriver.exe", options=webdriver_options)
#driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(1)

# 크롤링이 돌아가는 메인 함수
def do_crawling_by_google(language, key_word, news_Xpath):
  driver.get("https://google.com")

  search_bar = driver.find_element_by_name('q')
  search_bar.send_keys(key_word)
  time.sleep(1)
  search_bar.send_keys(Keys.ENTER)

  # xpath를 이용해 news 카테고리를 클릭하고자 할 때 검색어에 따라 xpath가 달라져서 임시로 xpath를 인자값으로 받음
  # 후에 이미지 인식을 이용하는 방식으로 개선할 예정
  news_tag = driver.find_element_by_xpath(news_Xpath)
  time.sleep(1)
  news_tag.click()
  time.sleep(3)
  # 뉴스 데이터 긁어온 후 josn파일 생성
  json_data = get_news_data_from_current_page(driver.page_source) # 이미지의 src 정보를 온전히 가져오기 위해 page_source이용
  create_json(language, json_data)

remove_all_file_in_forder(imgPath)
time.sleep(2)
do_crawling_by_google("kr", "우크라이나 교전 상황", "//*[@id='hdtb-msb']/div[1]/div/div[4]/a")
time.sleep(5)
do_crawling_by_google("en", "Ukraine engagement", "//*[@id='hdtb-msb']/div[1]/div/div[3]/a")
driver.close()