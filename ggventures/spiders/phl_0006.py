import scrapy


class Phl0006Spider(scrapy.Spider):
    name = 'phl_0006'
    allowed_domains = ['https://www.vsb.upd.edu.ph/']
    start_urls = ['http://https://www.vsb.upd.edu.ph//']

    def parse(self, response):
        pass
