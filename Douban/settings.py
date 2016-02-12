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
USER_AGENT = 'chrome'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY=0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=2
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Douban.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Douban.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Douban.pipelines.DoubanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

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

#specified xpath
ATTR_XPATH = {
    'movie_name':'/html/body/div[3]/div[1]/h1/span/text()',
    'movie_actor':'/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span[3]/span[2]/a/text()',
    'movie_type':'/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span[@property="v:genre"]/text()',
    'movie_date':'/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span[@property="v:initialReleaseDate"]/text()',
    'movie_rates':'/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()|/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/a/span/text()',
    'movie_desc':'//div[@id="link-report"]/span/text()',
}
