import scrapy


class Phl0002Spider(scrapy.Spider):
    name = 'phl_0002'
    allowed_domains = ['https://gsb.ateneo.edu/']
    start_urls = ['http://https://gsb.ateneo.edu//']

    def parse(self, response):
        pass
