import scrapy


class Deu0022Spider(scrapy.Spider):
    name = 'deu_0022'
    allowed_domains = ['https://www.goethe-business-school.de/en/']
    start_urls = ['http://https://www.goethe-business-school.de/en//']

    def parse(self, response):
        pass
