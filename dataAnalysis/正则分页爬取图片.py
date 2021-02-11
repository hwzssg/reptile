# 爬取糗图网站中糗图板块的图片数据
import requests
import re
import os

if __name__ == '__main__':
    # 创建文件夹，用来保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # 设置一个通用的url模板
    # for pageNum in range(1, 7):
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    for pageNum in range(1, 7):
        # 对应页码的url
        new_url = format(url % pageNum)
        # 使用通用爬虫对url对应的一整张页面进行爬取
        print(pageNum, new_url)
        page_text = requests.get(url=new_url, headers=headers).text
        # print(page_text)
        # 使用聚焦爬虫，将页面中所有图片进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)  # re.S单行匹配 re.M 多行匹配
        # print(img_src_list)
        for src in img_src_list:
            # 拼接出一个完整的图片url
            src = 'https:' + src
            # 请求到图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储路径
            imgPath = './qiutuLibs/' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                fp.close()
                print(img_name, '下载成功！！！')
