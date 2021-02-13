import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=&srcReferer=https://www.zhipin.com/']
    url = 'https://www.zhipin.com/c100010000/?query=python&page=%d'
    page_num = 2
    #回调函数接受item
    def parse_detail(self, response):
        item = response.meta['item']
        # //*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]
        # //*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div
        # job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        # //*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div
        job_desc = response.xpath('//*[@class="job-sec"]/div//text()').extract()
        job_desc = ''.join(job_desc)
        #print(job_desc)
        item['job_desc'] = job_desc
        yield item

    def parse(self, response):
        print(response)
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in li_list:
            item = BossproItem()
            # ./div/div[1]/div[1]/div/div[1]/span[1]/a
            job_name = li.xpath('./div/div[1]/div[1]/div//div[1]/span[1]/a/@title').extract_first()
            detail_url = 'https://www.zhipin.com' + li.xpath('./div/div[1]/div[1]/div//div[1]/span[1]/a/@href').extract_first()
            item['job_name'] = job_name
            print(job_name, detail_url)
            #对详情页发请求，获取详情页的源码数据
            #手动请求发送
            #请求传参，通过：meta={}，可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        #分页操作
        if self.page_num <= 3:
            new_url = format(self.url % self.page_num)
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)