##聚焦爬虫：
爬取页面中指定的页面内容
###编码流程：
- 指定url
- 发起请求
- 获取响应数据
- 数据解析(新增)
- 持久化存储
##数据解析分类：
- 正则
- bs4
- xpath(重点)
##数据解析原理概述
- 解析的局部文本内容都会在标签之间或者标签对应的属性中进行存储
- 1. 进行指定标签的定位
- 2. 标签或者标签对应的属性中存储的数据值进行提取(解析)

##图片数据爬取
<div class="thumb">

<a href="/article/124037297" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12403/124037297/medium/63YG1LGYISJ5OOSB.jpg" alt="糗事#124037297" class="illustration" width="100%" height="auto">
</a>
</div>

ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

##bs4进行数据解析
###数据解析原理
- 1.标签提取定位
- 2.提取标签，标签属性中存储的数据值
###bs4数据解析的原理:
- 1.实例化一个BeautifulSoup对象，并将页面源码数据加载到该对象中
- 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
###环境安装
- pip install bs4
- pip install lxml
###如何实例化BeautifulSoup对象
- from bs4 import BeautifulSoup
- 对象实例化
    1.将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    2.将互联网上获取的页面数据加载到该对象中
    page_text = response.text
    soup = BeautifulSoup(page_text, 'lxml')
 ###提供的用于数据解析的方法和属性 
- soup.tagName:返回的是文档中第一次出现tagName的标签
- soup.find():
    1.find('tagName'):等同于soup.tagName
    2.属性定位 find('tagName', class_='class')
- soup.find_all()
    返回符合要求的所有标签(列表)
- select
    select('某种选择器(id, class, 标签...)') #返回列表
    print(soup.select('body > div > div')[0]) #.wrapper 表示class为wrapper
    print(soup.select('body > div div')[0]) #空格表示多个层级，> 表示一个层级
- 获取标签中的文本数据
  soup.a.text/string/get_text()
  1. text/get_text()：可以获取某一个标签中所有的文本内容(不是直系也行)
  2. string 只可以获取某一个标签中直系的文本内容
- 获取标签中的属性值
  soup.a['href']
  
###获取网页编码格式
console下输入document.charset

##xpath解析：最常用最高效的一种解析方式。通用性。
###xpath解析原理
- 实现标签定位
    1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
    2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
- 环境安装
    1.pip install lxml
- 如何实例化etree对象 : from lxml import etree
    1.将本地html文档中的源码数据加载到etree对象中：
    etree.parse(filePath)
    2.将互连网上获取的源码数据加载到该对象中
    etree.HTML('page_text')
    3.xpath('xpath表达式') #学习表达式

###xpath表达式
- /:最左侧表示从根节点开始定位，后续表示一个层级 (/html/body/div)
- //:中间表示多个层级，最左侧表示从任意位置开始定位。
- 属性定位：//div[@class="header"] tag[@attrName="attrValue"]
- 索引定位：//div[@class="header"]/p[3] 索引从1开始
- 取文本：
  /text() 取得是标签当中直系的文本内容
  //text() 取得是标签当中非直系的文本内容
- 取属性：
  /@attrName ==>  img/src
  
##常用User-Agent
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11

##通用解决中文乱码的解决方案
text.encode('iso-8891-1').decode('gbk')