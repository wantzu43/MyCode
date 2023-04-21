import scrapy
import time
import random
from my1.items import My1Item   #關鍵句來自 item.py =My1Item

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/bbs/NBA/index.html']

    def parse(self, response):
        for i in range(10):
            time.sleep(1)
            url=f'http://www.ptt.cc/bbs/NBA/index{6500-i}.html'
            yield scrapy.Request(url,callback=self.parse_info)
            
    def parse_info(self,response):
        titles=response.xpath("//div[@class='title']/a/text()").extract()
        authors=response.xpath("//div[@class='meta']/div[@class='author']/text()").extract()            
        dates=response.xpath("//div[@class='meta']/div[@class='date']/text()").extract()
        for info in zip(titles,authors,dates):
            nba_item={
                'title':info[0],
                'author':info[1],
                'date':info[2]                               
                }
            yield nba_item