import scrapy


class Usa0064Spider(scrapy.Spider):
    name = 'usa_0064'
    allowed_domains = ['https://business.sdsu.edu/']
    start_urls = ['http://https://business.sdsu.edu//']

    def parse(self, response):
        pass
