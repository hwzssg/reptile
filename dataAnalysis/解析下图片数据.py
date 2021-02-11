import requests
from lxml import etree
import os

if __name__ == '__main__':
    if not os.path.exists('./游戏图片'):
        os.mkdir('./游戏图片')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    for suffix in range(1, 4):
        suffix = str(suffix)
        url = 'http://pic.netbian.com/4kyouxi/' + 'index_' + suffix + '.html'
        print(url)
        # url = 'http://pic.netbian.com/4kyouxi/'
        response = requests.get(url=url, headers=headers)
        response.encoding = 'GBK'
        page_text = response.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]//li')
        for li in li_list:
            img_url = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
            img_path = './游戏图片/' + li.xpath('./a/img/@alt')[0] + '.jpg'
            print(img_url, img_path)
            img_data = requests.get(url=img_url, headers=headers).content
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_path, '下载成功！！！')
