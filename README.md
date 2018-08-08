# pixiv_spider
a spider for pixiv daily top pictures
# 说明
这是一个用于爬取pixiv每日排行榜第一图片的爬虫
# 使用方法
## 注意事项
1. 使用前请自行加入pixiv的host
2. 爬虫使用了scrapy框架，请自行安装scrapy
3. 请自行添加 urllib，re
### host的添加
host路径一般为 C:\Windows\System32\drivers\etc，用记事本打开并复制黏贴（host于2018.7.6更新）：

    210.129.120.45 pixiv.net
    210.129.120.45 www.pixiv.net
    210.129.120.45 accounts.pixiv.net
    210.129.120.45 touch.pixiv.net
    210.129.120.49 www.pixiv.net
    210.129.120.49 accounts.pixiv.net
    210.129.120.49 touch.pixiv.net
    210.129.120.44 www.pixiv.net
    210.129.120.44 accounts.pixiv.net
    210.129.120.44 touch.pixiv.net
    210.140.131.144 source.pixiv.net
    210.140.131.45 imgaz.pixiv.net
    210.129.120.44 app-api.pixiv.net
    210.129.120.45 oauth.secure.pixiv.net
    210.129.120.41 dic.pixiv.net
    210.140.131.147 comic.pixiv.net
    210.129.120.45 factory.pixiv.net
    74.120.148.207 g-client-proxy.pixiv.net
    203.210.8.42 sketch.pixiv.net
    210.129.120.43 payment.pixiv.net
    210.129.120.40 sensei.pixiv.net
    210.140.131.145 novel.pixiv.net
    210.129.120.49 en-dic.pixiv.net
    210.140.131.145 i1.pixiv.net
    210.140.131.145 i2.pixiv.net
    210.140.131.145 i3.pixiv.net
    210.140.131.145 i4.pixiv.net
    210.140.131.159 d.pixiv.org
    210.140.92.135 pixiv.pximg.net
    210.140.92.136 i.pximg.net
    210.129.120.40 recruit.pixiv.net
## 使用
1. /acg/spiders/acg_spiders.py 内控制爬取日期
2. /acg/pipelines.py 内控制储存位置
3. 运行/entrypoint.py 开始爬虫
