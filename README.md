# pixiv_spider
a spider for pixiv daily top pictures
# 说明
这是一个用于爬取pixiv每日排行榜第一图片的爬虫
# 使用方法
## 注意事项
1. 使用前请自行加入pixiv的host
2. 爬虫使用了scrapy框架，请自行安装scrapy
3. 请自行添加 urllib，re，requests，os
### host的添加
host路径一般为 C:\Windows\System32\drivers\etc，用记事本打开并复制黏贴（host于2018.7.6更新）：

    #Pixiv
    210.129.120.52 www.pixiv.net
    210.140.131.144 source.pixiv.net
    210.129.120.42 accounts.pixiv.net
    210.140.131.144 imgaz.pixiv.net

## 使用
1. /acg/spiders/acg_spiders.py 内控制爬取日期
2. /acg/pipelines.py 内控制储存位置
3. 运行/entrypoint.py 开始爬虫

### 其他
pixiv关注画师图片下载链接：
[https://github.com/allenx555/pixiv_downloader]()
