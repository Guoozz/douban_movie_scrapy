#介绍
使用scrapy框架爬取豆瓣电影
#如何使用
```sh
git clone https://github.com/Guoozz/douban_movie_scrapy.git
cd douban_movie_scrapy
scrapy crawl douban_movie
```
#爬取的信息在哪里
保存在mongo数据库中
#注意事项
必须安装[scrapy](scrapy.org)框架
安装方法很简单,在终端下输入
```sh
pip install scrapy
```
需要安装[Pillow](https://pillow.readthedocs.org/en/latest/handbook/tutorial.html)
```sh
pip install pillow
```
#Version
###0.1
参考scrapy官方tutorial写的第一个爬虫，功能很基础。爬取1000多部电影后
request被重定向或出现403error
###0.11
在继承CrawlSpider的基础上进行代码重构,代码结构更清晰，依然没有解决403or301error
###0.12
将爬取的数据保存在mongo数据库中，去除冗余代码
###1.0
加入**Douban.middlewares.DoubanCaptchaDownloadMiddleware**类处理403验证码，
当网站需要验证码时，会自动打开验证码图片，在终端中输入验证码，爬虫会继续运行
###1.01
设置爬虫中间状态保存路径
###1.02
添加ItemLoader对提取的信息进行过滤
###1.1
解决并发请求下，返回多个验证码的问题。
添加对导演，别名等信息的爬取
