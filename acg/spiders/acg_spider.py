# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 0026 20:12
# @Author  : allenx555
# @FileName: acg_spider.py
# @Software: PyCharm

import scrapy
from scrapy.http import Request
from acg.items import AcgItem
import urllib
import re


class acgSpider(scrapy.Spider):

    name = "acg"
    bash_url = "https://www.pixiv.net/ranking.php?mode=daily&date="
    start_urls = []
    allowed_domains = ['pixiv.net', 'piximg.net']
    # for i in range(20080100, 20081200, 100):  # 爬取的时间范围，可以用i控制年份j控制日期以爬取一整年
    for j in range(20180601, 20180631):  # 爬取的时间范围，可以用j控制日期爬取固定月份
        start_urls.append(bash_url + str(j))

    def parse(self, response):
        acg_xpath = str(
            response.xpath('//*[@id="1"]/@data-id').extract())
        ids = acg_xpath.replace("['", "").replace("']", "")
        url = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + ids
        yield Request(url, callback=self.get_picture)

    def get_picture(self, response):
        picture_xpath = response.xpath('/html/body/div[6]/div/div[2]/div/div/div[1]/div[2]/a/img/@src').extract()
        picture_bash_url = (str(picture_xpath)).replace(
            "['https://i.pximg.net/c/600x600/img-master/", "").replace("_master1200.jpg']", "")
        url = "https://i.pximg.net/img-original/" + picture_bash_url + ".jpg"
        reg = r'.+/(\d+)_p0'
        picture_id = re.findall(reg, url)[0]
        Reference = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + picture_id

        Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                   'Connection': 'keep-alive',
                   'Referer': Reference
                   }

        try:
            req = urllib.request.Request(url, None, Headers)
            res = urllib.request.urlopen(req, timeout=1)
            res.close()
            item = AcgItem()
            item['image_form'] = ['.jpg']
        except urllib.error.HTTPError:
            url = url.replace('.jpg', '.png')
            req = urllib.request.Request(url, None, Headers)
            res = urllib.request.urlopen(req, timeout=1)
            res.close()
            item = AcgItem()
            item['image_form'] = ['.png']

        item['image_urls'] = [url]
        item['image_referer'] = [Reference]
        item['image_name'] = [picture_id]

        return item

