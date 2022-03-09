import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def public_broadcasting(url, xpath, category):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get(url)

    link_tags = driver.find_elements_by_xpath(xpath)

    datas = []
    for i in range(3):
        link = link_tags[i].get_attribute('href')
        if category == 'BBC':
            # title_html: <h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">Russia soon unable to pay its debts, warns agency</h3>
            title_html = link_tags[i].get_attribute('innerHTML')
            title = title_html[title_html.find('>') + 1:title_html.find('</')]
        elif category == 'ZDF':
            title = link_tags[i].find_element_by_tag_name('span').text

        datas.append({"name": title, "link": link, "category": category})

    with open(f'./stopwar/crawlingData/{category}.json', 'w', encoding='utf-8') as outfile:
        json.dump(datas, outfile, indent=4)

    driver.quit()
    print('Done')


bbc_url = 'https://www.bbc.com/news/world-60525350'
bbc_xpath = '//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div/div/div/div/a'
bbc_catagory = 'BBC'

zdf_url = 'https://www.zdf.de/nachrichten/politik'
zdf_xpath = '//*[@id="skip-main"]/div[2]/section[1]/div/div/article/div/div/h3/a'
zdf_catagory = 'ZDF'

public_broadcasting(bbc_url, bbc_xpath, bbc_catagory)
public_broadcasting(zdf_url, zdf_xpath, zdf_catagory)
