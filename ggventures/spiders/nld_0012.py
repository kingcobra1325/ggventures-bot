import scrapy


class Nld0012Spider(scrapy.Spider):
    name = 'nld_0012'
    allowed_domains = ['https://abs.uva.nl/']
    start_urls = ['http://https://abs.uva.nl//']

    def parse(self, response):
        pass
