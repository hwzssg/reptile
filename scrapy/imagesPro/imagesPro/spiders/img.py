import scrapy
from imagesPro.items import ImagesproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 反爬机制 图片懒加载 不在可视化界面的图片属性key为src2
            # src = div.xpath('./div/a/img/@src').extract_first()
            # 使用伪属性
            src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            print(src)
            item = ImagesproItem()
            item['src'] = src
            yield item
