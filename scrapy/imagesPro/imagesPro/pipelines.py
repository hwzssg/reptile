# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline
import scrapy
# class ImagesproPipeline:
#     def process_item(self, item, spider):
#         return item

class CImagesPipeLine(ImagesPipeline):
    #重写父类三种方法
    #就是根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        #print('get_media_requests', item)
        yield scrapy.Request(item['src'])
    #指定图片存储的路径
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.url.split('/')[-1]
        #print(file_name)
        return file_name
    def item_completed(self, results, item, info):
        #print('item_completed', item)
        return item #返回下一个即将被执行的管道类
