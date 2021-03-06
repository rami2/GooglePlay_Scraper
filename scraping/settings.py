# -*- coding: utf-8 -*-

# Scrapy settings for gplaycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'app'

SPIDER_MODULES = ['scraping.spiders']
NEWSPIDER_MODULE = 'scraping.spiders'
#FEED_FORMAT = 'csv'
#FEED_URI = 'something.csv'
USER_AGENT = 'Your Name and your github)'
ITEM_PIPELINES = {
    'scraping.pipelines.GPlayPipeline': 400,
    'scraping.pipelines.MongoPipeline': 300,
}
MONGO_URI = 'Your mongo db uri eg: mongodb://user:pass@server(localhost if local)/db name'
MONGO_DATABASE = 'DB name'

REACTOR_THREADPOOL_MAXSIZE = 20
# LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
##RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 60
##REDIRECT_ENABLED = False
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
