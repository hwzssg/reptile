from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    #在首页中解析出章节的标题和详情页的url
    #1.实例化一个BeautifulSoup对象，需要将源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    #print(li_list)
    fp = open('三国.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/' + li.a['href']
        #对详情页发起请求，解析章节内容
        detail_response = requests.get(url=detail_url, headers=headers)
        detail_response.encoding = 'utf-8'
        detail_page_text = detail_response.text
        #解析出详情页面中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        #解析到章节的内容
        content = div_tag.text
        #持久化存储
        fp.write(title + ': ' + content + '\n')
        print(title, '爬取成功！！！')