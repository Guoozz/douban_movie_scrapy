#介绍
使用scrapy框架爬取豆瓣电影
#如何使用
```sh
git clone https://github.com/Guoozz/douban_movie_scrapy.git
cd douban_movie_scrapy
scrapy crawl douban_movie
```
#爬取的信息在哪里
douban_movie_scrapy根目录下**douban_movie.json**文件
#注意事项
必须安装[scrapy](scrapy.org)框架
安装方法很简单,在终端下输入
```sh
pip install scrapy
```
#Version
0.1 参考scrapy官方tutorial写的第一个爬虫，功能很基础。爬取1000多部电影后
request被重定向或出现403error
