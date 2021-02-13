import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    #allowed_domains = ['http://www.521609.com/meinvxiaohua/']
    start_urls = ['http://www.521609.com/meinvxiaohua/']
    #生成一个通用的url模板
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a[2]/b/text() | ./a[2]/text()').extract_first()
            print(img_name)
        print('----------------------------------')
        if self.page_num <= 11:
            news_url = format(self.url % self.page_num)
            self.page_num += 1
            #手动请求发送，callback回调函数是专门用于数据解析
            yield scrapy.Request(url=news_url, callback=self.parse)