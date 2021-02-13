import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['https://www.qiushibaike.com/text/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #print(response.text)
        #解析：作者名称 + 端子内容
        #'//*[@id="content"]/div/div[2]'
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []
        for div in div_list:
            #xpath返回的是列表，列表元素一定为Selector类型的对象
            #Selector对象的extract方法可以将对象中data参数存储的字符串提取出来
            #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            #extract_first()只有一个元素
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            #列表调用了extract()之后，则表示将列表中每一个Selector对象中data对应的字符串
            #提取出来
            content = div.xpath('./a/div/span//text()').extract() # //text() 获取所有子标签中text内容
            #列表转成多字符串组合
            content = ''.join(content)
            dic = {
                'author': author,
                'content': content,
            }
            all_data.append(dic)
            # print(author, content)
        #基于终端格式的持久化存储
        return all_data

