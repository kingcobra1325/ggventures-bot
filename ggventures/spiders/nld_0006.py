import scrapy


class Nld0006Spider(scrapy.Spider):
    name = 'nld_0006'
    allowed_domains = ['https://www.nyenrode.nl/']
    start_urls = ['http://https://www.nyenrode.nl//']

    def parse(self, response):
        pass
