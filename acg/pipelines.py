# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import requests


class AcgPipeline(object):

    def process_item(self, item, spider):
        url = item['image_urls'][0]
        reference = item['image_referer'][0]

        Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                   'Connection': 'keep-alive',
                   'Referer': reference,
                   }
        image = requests.get(url, headers=Headers)
        form = item['image_form'][0]
        name = item['image_name'][0]
        path = 'D://Project_pixiv/acg/test/2018/2018.6/' + name + form  # 引号内部为图片储存地址
        f = open(path, "wb")
        f.write(image.content)
