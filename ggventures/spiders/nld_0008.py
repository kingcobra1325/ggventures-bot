import scrapy


class Nld0008Spider(scrapy.Spider):
    name = 'nld_0008'
    allowed_domains = ['https://www.rsm.nl/']
    start_urls = ['http://https://www.rsm.nl//']

    def parse(self, response):
        pass
