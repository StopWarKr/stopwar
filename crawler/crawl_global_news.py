import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)

kbs_url = 'https://search.kbs.co.kr/?keyword=%EC%9A%B0%ED%81%AC%EB%9D%BC%EC%9D%B4%EB%82%98'
nhk_url = 'https://www3.nhk.or.jp/news/special/ukraine/?cid=oshirase'

json_data = []

def createJson(category, ): # json 파일로 변경 ./stopwar/crawlingData/
  with open(f'./stopwar/crawlingData/{category}.json', 'w', encoding = 'UTF-8-sig') as f_write:
    json.dump(json_data, f_write, ensure_ascii = False, indent = 4)


def crawl_global_news(url, category, count): # count 만큼 가져 오기
    json_data = []
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    if (category == 'KBS'):

        for i in range(0, count): 
            title = soup.select('ul#search_replay_list > li > a')[i].text
            link = 'https://vod.kbs.co.kr' + soup.select('ul#search_replay_list > li > a')[i]['href']
            json_data.append({ '제목': title, '링크' : link })
        
        with open(f'{category}.json.', 'w', encoding = "UTF-8-sig") as f_write:
            json.dump(json_data, f_write, ensure_ascii = False, indent = 4)
          
    if (category == 'NHK'):

        for i in range(0, count): 
            title = soup.select('dd')[i].text
            link = soup.select('ul.p-attention__list > li > a')[i]['href']
            json_data.append({ '제목': title, '링크' : link} )

        with open(f'./stopwar/crawlingData/{category}.json', 'w', encoding = 'UTF-8-sig') as f_write:
            json.dump(json_data, f_write, ensure_ascii = False, indent = 4)




    
    




crawl_global_news(kbs_url, 'KBS', 3)
crawl_global_news(nhk_url, 'NHK', 3)
