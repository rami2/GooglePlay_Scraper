# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

import scrapy

class GplayItem(scrapy.Item):

    App_name = scrapy.Field()
    Developer = scrapy.Field()
    Downloads = scrapy.Field()
    Developer_EMail = scrapy.Field()
    Genre = scrapy.Field()
    Rating_value = scrapy.Field()
    Review_number = scrapy.Field()



