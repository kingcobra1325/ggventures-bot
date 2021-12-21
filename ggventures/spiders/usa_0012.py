import scrapy


class Usa0012Spider(scrapy.Spider):
    name = 'usa_0012'
    allowed_domains = ['https://www.csuchico.edu/cob/']
    start_urls = ['http://https://www.csuchico.edu/cob//']

    def parse(self, response):
        pass
