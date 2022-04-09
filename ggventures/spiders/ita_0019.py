import scrapy


class Ita0019Spider(scrapy.Spider):
    name = 'ita_0019'
    allowed_domains = ['https://www.unibo.it/en']
    start_urls = ['http://https://www.unibo.it/en/']

    def parse(self, response):
        pass
