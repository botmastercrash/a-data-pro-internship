# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    productNumber = scrapy.Field()
    productName = scrapy.Field()
    productStore = scrapy.Field()
    imgForProductLink = scrapy.Field()
    urlLink = scrapy.Field()
    isProductAvailable = scrapy.Field()
    productPrice = scrapy.Field()