import scrapy


class Deu0017Spider(scrapy.Spider):
    name = 'deu_0017'
    allowed_domains = ['https://www.wiwi.kit.edu/english/']
    start_urls = ['http://https://www.wiwi.kit.edu/english//']

    def parse(self, response):
        pass
