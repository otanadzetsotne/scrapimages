# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class DownloaderPipeline:
    def process_item(self, item, spider):
        return item


# Pre created pipeline for images downloading
# listens items objects with image_urls and images properties
class DownloaderImagesPipeline(ImagesPipeline):
    pass
