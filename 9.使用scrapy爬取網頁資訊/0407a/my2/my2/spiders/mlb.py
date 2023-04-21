import scrapy


class MlbSpider(scrapy.Spider):
    name = 'mlb'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/MLB/index.html']

    def parse(self, response):
        titles = response.xpath("//div[@class='title']/a/text()").extract()
    
        authors = response.xpath("//div[@class='meta']/div[@class='author']/text()").extract()
        
        for t,a in zip(titles,authors):
            print('標題:',t)
            print('作者:',a)
