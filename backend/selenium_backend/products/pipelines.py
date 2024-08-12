# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

    
# class ProductsPipeline(object):
#     def process_item(self, item, spider):
#         item.save()
#         return item

from asgiref.sync import sync_to_async
from scrapy.exceptions import DropItem

class ProductsPipeline(object):
    async def process_item(self, item, spider):
        if item['price'] is None:
            # You can set a default value or raise DropItem to skip the item
            item['price'] = 'not found'

        # Save the new item
        await sync_to_async(item.save)()
        return item

