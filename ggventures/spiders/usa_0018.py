import scrapy


class Usa0018Spider(scrapy.Spider):
    name = 'usa_0018'
    allowed_domains = ['https://mason.wm.edu/']
    start_urls = ['http://https://mason.wm.edu//']

    def parse(self, response):
        pass
