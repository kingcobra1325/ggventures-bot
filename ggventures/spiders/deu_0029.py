import scrapy


class Deu0029Spider(scrapy.Spider):
    name = 'deu_0029'
    allowed_domains = ['https://www.uni-osnabrueck.de/en/home/']
    start_urls = ['http://https://www.uni-osnabrueck.de/en/home//']

    def parse(self, response):
        pass
