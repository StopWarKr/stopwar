from common.google_crawler import GoogleCrawler

GoogleCrawler('후원').crawl_news('Ukraine Sponsor',
                               3).write_json('en_SponsorNewsData')

GoogleCrawler('후원').crawl_news(
    '우크라이나 후원', 3).write_json('kr_SponsorNewsData')
