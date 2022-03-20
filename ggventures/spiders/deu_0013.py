import scrapy


class Deu0013Spider(scrapy.Spider):
    name = 'deu_0013'
    allowed_domains = ['https://www.hu-berlin.de/en']
    start_urls = ['http://https://www.hu-berlin.de/en/']

    def parse(self, response):
        pass
