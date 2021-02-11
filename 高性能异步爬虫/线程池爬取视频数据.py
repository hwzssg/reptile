#部分解析 https://blog.csdn.net/qq_36807888/article/details/109841043

import requests
from lxml import etree
import re
import random
from multiprocessing.dummy import Pool
import os

if not os.path.exists('./video'):
    os.mkdir('./video')
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
def download_video(video_info):
    './video/陈佩斯开腔 | 在历史中寻找中国喜剧的踪迹.mp4'
    with open('./video/' + video_info['name'], 'wb') as fp:
        print('./video/' + video_info['name'], ' downloading...')
        video = requests.get(url=video_info['url'], headers=headers).content
        fp.write(video)
        print(video_info['name'], ' download successed!!!')

#爬取梨视频中视频数据

#原则：线程池处理的是阻塞且耗时的操作
#对下述url发起请求，解析出视频详情页的url和视频名称
session = requests.Session()
url = 'https://www.pearvideo.com/category_4'
response = session.get(url=url, headers=headers)
response.encoding= 'UTF-8'
page_text = response.text

tree = etree.HTML(page_text)

li_list = tree.xpath('//*[@id="categoryList"]/li')
#li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
video_name_urls = []

for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    #print(detail_url, name)
    #对详情页的url发起请求
    ret = session.get(url=detail_url, headers=headers)
    ret.encoding = 'UTF-8'
    detail_page_text = ret.text
    #从详情页面中解析出视频的地址(url)
    ex = ',contId = "(.*?)",commentLoad'
    contId = re.findall(ex, detail_page_text)[0]
    #改为ajax请求
    mrd = str(random.random())
    #referer = 'https://www.pearvideo.com/video_' + contId
    #ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + contId + '&mrd=' + mrd
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp'
    #print(ajax_url)
    params = {
        'contId': contId,
        'mrd': mrd,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        #'Referer': referer,
        'Referer': detail_url,
    }
    #真实url解析
    data = session.get(url=ajax_url, params=params, headers=headers).json()
    head_url = data['videoInfo']['videos']['srcUrl'].rsplit('/', 1)[0] + '/cont-'
    end_url = '-' + data['videoInfo']['videos']['srcUrl'].split('-', 1)[-1]
    real_url = head_url + contId + end_url
    #print(data['videoInfo']['videos']['srcUrl'], real_url)
    info = {
        'url' : real_url,
        'name': name,
    }
    video_name_urls.append(info)

print(video_name_urls)
pool = Pool(4)
pool.map(download_video, video_name_urls)
pool.close()
pool.join()
