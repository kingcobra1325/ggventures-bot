import scrapy


class Usa0094Spider(scrapy.Spider):
    name = 'usa_0094'
    allowed_domains = ['https://business.utulsa.edu/']
    start_urls = ['http://https://business.utulsa.edu//']

    def parse(self, response):
        pass
