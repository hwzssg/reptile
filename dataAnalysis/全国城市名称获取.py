import requests
from lxml import etree
import os

if __name__ == '__main__':
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # response = requests.get(url=url, headers=headers)
    # response.encoding = 'UTF-8'
    # page_text = response.text
    #
    # tree = etree.HTML(page_text)
    # hot_li_list = tree.xpath('//div[@class="hot"]/div[2]/ul/li')
    # all_city_name = []
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(hot_city_name)
    # all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in all_li_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_name.append(city_name)
    # print(all_city_name)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    response = requests.get(url=url, headers=headers)
    response.encoding = 'UTF-8'
    page_text = response.text

    all_city_name = []
    tree = etree.HTML(page_text)
    all_li_list = tree.xpath('//div[@class="hot"]/div[2]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    for li in all_li_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_name.append(city_name)
    print(all_city_name, len(all_city_name))