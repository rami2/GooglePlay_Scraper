from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scraping.items import GplayItem
import urlparse

class MySpider(CrawlSpider):
  name = "apps"
  allowed_domains = ["play.google.com"]
  start_urls = ["https://play.google.com/store/apps/"]
  rules = [Rule(LinkExtractor(allow=(r'details\?',),deny=(r'reviewId')),follow=True,callback='parse_link')]
  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('//head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)
    
  def parse_link(self,response):
      hxs = Selector(response)
      titles = hxs.xpath('/html')
      items = []
      for titles in titles :
        item = GplayItem()
        item["App_name"] = ''.join(titles.xpath('//h1[@itemprop="name"]/span/text()').extract())
        item["Developer"] = ''.join(titles.xpath('//a[@class="hrTbp R8zArc"]/text()').extract())
        item["Downloads"] = ''.join(titles.xpath('//div[@class="hAyfc"][3]/span[@class="htlgb"]/div/span/text()').extract())
        item["Developer_EMail"] = hxs.xpath('//body').re_first('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
        item["Genre"] = ''.join(titles.xpath('//*[@itemprop="genre"]/text()').extract())
        item["Rating_value"] = titles.xpath('//div[@class="pf5lIe"]/div/@aria-label').extract_first()
        item["Review_number"] = ''.join(titles.xpath('//span[@class="AYi5wd TBRnV"]/span[@class=""]/text()').extract())

        items.append(item)
      return items
      

