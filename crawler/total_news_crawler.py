from common.google_crawler import GoogleCrawler
from common.en_HistoryNewsData import ukraineHistory_en
import time

# error가 나는 이유는 google 크롤링을 너무 많이 해서입니다.
# 시간단위로 끊던가, 개수를 줄이면 정상 작동합니다.
# try:
#     GoogleCrawler('교전 최신 상황').crawl_news('ukraine belligerence', 2).write_json('en_BattleNewsData')
#     print('en_BattleNewsData')
# except:
#     print('en_BattleNewsData error')

try:
    GoogleCrawler('교전 최신 상황').crawl_news('우크라이나 교전 상황', 2).write_json('kr_BattleNewsData')
    print('kr_BattleNewsData')
except Exception as e:
    print(e)
    print('kr_BattleNewsData error')

time.sleep(3);

# TODO :이 사이트만 크롤링이 타 사이트인데 수정 여부 논의 필요
# try:
#     ukraineHistory_en('ukraine', 2, 'en_HistoryNewsData', '역사')
#     print('en_HistoryNewsData')
# except:
#     print('en_HistoryNewsData error')

try:
    GoogleCrawler('역사').crawl_news('우크라이나 역사', 2).write_json('kr_HistoryNewsData')
    print('kr_HistoryNewsData')
except:
    print('kr_HistoryNewsData error')

time.sleep(3);

# try:
#     GoogleCrawler('규제').crawl_news('ukraine regulation', 2).write_json('en_RegulationNewsData')
#     print('en_RegulationNewsData')
# except:
#     print('en_RegulationNewsData error')

try:
    GoogleCrawler('규제').crawl_news('우크라이나 규제', 2).write_json('kr_RegulationNewsData')
    print('kr_RegulationNewsData')
except Exception as e:
    print(e)
    print('kr_RegulationNewsData error')

time.sleep(3);

# try:
#     GoogleCrawler('후원').crawl_news('Ukraine Sponsor', 2).write_json('en_SponsorNewsData')
#     print('en_SponsorNewsData')
# except:
#     print('en_SponsorNewsData error')

try:
    GoogleCrawler('후원').crawl_news('우크라이나 후원', 2).write_json('kr_SponsorNewsData')
    print('kr_SponsorNewsData')
except Exception as e:
    print(e)
    print('kr_SponsorNewsData error')

time.sleep(3);

# try:
#     GoogleCrawler('협상 진행 과정').crawl_news('ukraine negotiation progress situation', 2).write_json('en_NegoNewsData')
#     print('en_NegoNewsData')
# except:
#     print('en_NegoNewsData error')

try:
    GoogleCrawler('협상 진행 과정').crawl_news('우크라이나 협상 진행 상황', 2).write_json('kr_NegoNewsData')
    print('kr_NegoNewsData')
except Exception as e:
    print(e)
    print('kr_NegoNewsData error')

time.sleep(3);

# try:
#     GoogleCrawler('지역 라이브 상황').crawl_news('ukraine local live', 2).write_json('en_LocalNewsData')
#     print('en_LocalNewsData')
# except:
#     print('en_LocalNewsData error')

try:
    GoogleCrawler('지역 라이브 상황').crawl_news('우크라이나 실시간 상황', 2).write_json('kr_LocalNewsData')
    print('kr_LocalNewsData')
except Exception as e:
    print(e)
    print('kr_LocalNewsData error')

time.sleep(3);

# try:
#     GoogleCrawler('피해 상황').crawl_news('ukraine damage', 2).write_json('en_DamageNewsData')
#     print('en_DamageNewsData')
# except:
#     print('en_DamageNewsData error')

try:
    GoogleCrawler('지역 라이브 상황').crawl_news('우크라이나 피해 상황', 2).write_json('kr_DamageNewsData')
    print('kr_DamageNewsData')
except Exception as e:
    print(e)
    print('kr_DamageNewsData error')