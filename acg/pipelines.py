# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import requests


class AcgPipeline(object):

    def process_item(self, item, spider):
        for url in item['image_urls']:
            url = url
        for reference in item['image_referer']:
            reference = reference

        Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                   'Connection': 'keep-alive',
                   'Referer': reference,
                   }
        image = requests.get(url, headers=Headers)
        for form in item['image_form']:
            form = form
        for name in item['image_name']:
            name = name
        path = 'D://Project_pixiv/acg/test/2018/2018.6/' + name + form  # 引号内部为图片储存地址
        f = open(path, "wb")
        f.write(image.content)
