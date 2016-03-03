# -*- coding: utf-8 -*-

# Scrapy settings for Douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Douban'

SPIDER_MODULES = ['Douban.spiders']
NEWSPIDER_MODULE = 'Douban.spiders'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=8

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY=0.25
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN=1
# CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

    'Cache-Control':'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Connection': 'keep-alive',
    'Cookie':'bid="gEWWmL+aujk"; ll="108088"; ps=y; ue="765422564@qq.com"; ct=y; push_noty_num=0; push_doumail_num=6; __utmt=1; _pk_id.100001.8cb4=4f3bc6a893a95484.1455435988.10.1455670781.1455668573.; _pk_ses.100001.8cb4=*; __utma=30149280.2098868936.1455270556.1455666792.1455670749.16; __utmb=30149280.2.10.1455670749; __utmc=30149280; __utmz=30149280.1455270556.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.6666; ap=1',
    'Upgrade-Insecure-Requests':'1',
}

# REDIRECT_ENABLED = False
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Douban.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Douban.middlewares.DoubanCaptchaMiddleware': 1,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Douban.pipelines.DoubanPipeline':300,
    'scrapy.pipelines.images.ImagesPipeline':301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
# AUTOTHROTTLE_ENABLED=True
# The initial download delay
# AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY=300
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG=True

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

#mongoDB settings 
MONGO_URI = '127.0.0.1'
MONGO_DATABASE = 'douban'
MONGO_COLLECTION = 'movies'

#specified xpath
INFO_XPATH = {
    'name':'//span[@property="v:itemreviewed"]/text()',
    'actor':'//a[@rel="v:starring"]/text()',
    'types':'//span[@property="v:genre"]/text()',
    'date':'//span[@property="v:initialReleaseDate"]/text()',
    'desc':'//div[@id="link-report"]/span/text()',
    'director':'//div[@id="info"]/span[1]/span[2]/a/text()',
    'writer':'//div[@id="info"]/span[2]/span[2]/a/text()',
    'length':'//span[@property="v:runtime"]/text()',
}

RE = {
    'alias':u'又名:(.+)',
    'region':u'地区:(.+)',
    'language':u'语言:(.+)',
}

RATE_XPATH = {
    'stars':'//span[@class="rating_per"]/text()',
    'num':'//span[@property="v:votes"]/text()',
    'average':'//strong[@property="v:average"]/text()',
}

#JOBDIR='states/movies'
IMAGES_STORE = 'covers'
ALLOW_COVER = False
