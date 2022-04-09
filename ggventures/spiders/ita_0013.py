import scrapy


class Ita0013Spider(scrapy.Spider):
    name = 'ita_0013'
    allowed_domains = ['http://www.stoa.it/sito/']
    start_urls = ['http://http://www.stoa.it/sito//']

    def parse(self, response):
        pass
