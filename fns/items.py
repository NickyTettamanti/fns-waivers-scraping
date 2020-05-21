# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FnsItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    request = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()
    jurisdiction = scrapy.Field()

    # Todo: If possible, integrate URL for pdf.
    # pdf_request = scrapy.Field()

    pass
