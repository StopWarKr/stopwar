from common.google_crawler import GoogleCrawler

GoogleCrawler('규제').crawl_news('ukraine regulation',
                               3).write_json('en_RegulationNewsData')

GoogleCrawler('규제').crawl_news(
    '우크라이나 규제', 3).write_json('kr_RegulationNewsData')
