# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# Todo: Add pipeline to clean data.
# Some of the output (i.e. status, waiver request) will be a list where [0] is
# what we want to have, and [1] is additional ifnormation (i.e. a link to an approved waiver).
# We need to clean each item in this pipeline.

class FnsPipeline(object):
    def process_item(self, item, spider):
        return item
