import scrapy


class Nld0009Spider(scrapy.Spider):
    name = 'nld_0009'
    allowed_domains = ['https://www.tias.edu/en']
    start_urls = ['http://https://www.tias.edu/en/']

    def parse(self, response):
        pass
