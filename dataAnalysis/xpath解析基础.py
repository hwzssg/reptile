# 爬取糗图网站中糗图板块的图片数据
import requests
from lxml import etree

if __name__ == '__main__':
    # 设置一个通用的url模板
    # for pageNum in range(1, 7):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    #实例化好一个etree对象，且被解析的源码加载到该对象中
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('化妆品.html', parser=parser)
    #r = tree.xpath('/html/head/meta')
    #r = tree.xpath('//div')
    #r = tree.xpath('//div[@class="hzbtabs"]/span[2]/text()')
    r = tree.xpath('//div[@class="hzbtabs"]/span[2]/@id')
    print(r)
    r = tree.xpath('//div[@class="hzbtabs"]/span[2]/@dataid')
    print(r)
