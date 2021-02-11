import requests
from lxml import etree
import json
#爬取58二手房房源
if __name__ == '__main__':

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }

    #url = 'https://hz.58.com/ershoufang/'
    #page_text = requests.get(url=url, headers=headers1).text
    #数据解析
    #tree = etree.HTML(page_text)
    #data = tree.xpath('//section[@class="list"]//div[@class="property-content-title"]')
    #print(data)

    #实例化好一个etree对象，且被解析的源码加载到该对象中
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('58二手房.html', parser=parser)

    #data = tree.xpath('//section[@class="list"]//div[@class="property-content-title"]/h3/@title')
    datas = tree.xpath('//section[@class="list"]//div[@class="property-content-title"]/h3/text()')
    print(datas)
    fp = open('58房1.txt', 'w', encoding='utf-8')
    for data in datas:
        fp.write(data + '\n')
    fp1 = open('58房2.txt', 'w', encoding='utf-8')
    json.dump(datas, fp=fp1, ensure_ascii=False)
    fp1.close()