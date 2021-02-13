import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称：爬虫源文件的唯一标识
    name = 'first'
    #允许的域名：用来限定start_urls列表中哪些url可以进行请求发送
    # allowed_domains = ['www.baidu.com'] #一般不用，某些资源在另外链接中
    #起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['http://www.baidu.com/', 'https://www.sogou.com']

    #用作数据解析，response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):
        print(response1)
