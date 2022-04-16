import scrapy


class Nld0007Spider(scrapy.Spider):
    name = 'nld_0007'
    allowed_domains = ['https://www.ou.nl/en/faculty-of-management']
    start_urls = ['http://https://www.ou.nl/en/faculty-of-management/']

    def parse(self, response):
        pass
