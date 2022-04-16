import scrapy


class Nld0010Spider(scrapy.Spider):
    name = 'nld_0010'
    allowed_domains = ['https://tsm.nl/']
    start_urls = ['http://https://tsm.nl//']

    def parse(self, response):
        pass
