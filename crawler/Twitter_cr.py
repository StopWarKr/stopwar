from bs4 import BeautifulSoup
import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import googletrans

translator = googletrans.Translator()

User_Agent_head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def createJson(category, json_data): # json 파일로 변경 ./stopwar/crawlingData/
  with open(f'./stopwar/crawlingData/{category}.json', 'w', encoding = 'UTF-8-sig') as f_write:
    json.dump(json_data, f_write, ensure_ascii = False, indent = 4)


def do_crawling(_my_driver, _count):
    _my_driver.get("https://twitter.com/ZelenskyyUa")
    time.sleep(2) # 로딩 시간 기다리기
    for i in range(0, _count):
        time.sleep(1)
        _my_driver.execute_script(f"window.scrollTo(0, {i * 250})") # 스크롤 내리기
        soup = BeautifulSoup(_my_driver.page_source, 'html.parser')
        time.sleep(1)
        tag = soup.find_all('div', attrs={'class' : 'css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu'})[i]
        # print(i)
        time.sleep(1)
        
        # class로 안 가져와져서 자식으로 가져오기.
        text_spans_parent = tag.findChildren('div', recursive=False)[1]
        text_spans_parent = text_spans_parent.findChildren('div', recursive=False)[0]
        text_spans_parent = text_spans_parent.findChildren('div', recursive=False)[0]

        time.sleep(1)
        text_spans = text_spans_parent.find_all('span') # 내용 가져오기
        _year, _month, _date = soup.select("time")[0]['datetime'].split("T")[0].split("-") # 2022-04-10T12:04:06.000Z <- 이런 형식 이여서 2번 스플릿 해서 year,month,date를 가져옴
        # print("\n\n\n\n\n")
        # print("-" * 100)
        json_data = []
        dates =_month + "월" + _date + "일"
        ukraine_text = ""
        
        
        for span in text_spans: 
            # print(translator.translate(span.get_text(), dest = "ko").text)
            ukraine_text += span.get_text() # 글 내용에 이모티콘 때문에 문장 중간이 짤려서 더한다.
            # print(ukraine_text)
            
        korea_text = translator.translate(ukraine_text, dest = "ko").text

        json_data.append({ 'description': ukraine_text, 'date' : dates,'description_ko': korea_text ,"catagory": "트위터",} )

        createJson("Twitter", json_data)
        print("-" * 100)
    print("\n\n\n\n\n")


def get_driver():
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    time.sleep(1)
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=webdriver_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(1)
    return driver


do_crawling(get_driver(), 2)