# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FnsItem(scrapy.Item):
    # define the fields for your item here like:
    program = scrapy.Field()
    jurisdiction = scrapy.Field()
    date = scrapy.Field()
    request = scrapy.Field()
    request2 = scrapy.Field()
    request_receive = scrapy.Field()
    status = scrapy.Field()


    # Todo: If possible, integrate URL for pdf.
    # pdf_request = scrapy.Field()

    pass
