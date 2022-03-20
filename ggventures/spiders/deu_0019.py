import scrapy


class Deu0019Spider(scrapy.Spider):
    name = 'deu_0019'
    allowed_domains = ['https://uni-bayreuth.de/en']
    start_urls = ['http://https://uni-bayreuth.de/en/']

    def parse(self, response):
        pass
