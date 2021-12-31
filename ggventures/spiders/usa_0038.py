import scrapy


class Usa0038Spider(scrapy.Spider):
    name = 'usa_0038'
    allowed_domains = ['https://carey.jhu.edu/']
    start_urls = ['http://https://carey.jhu.edu//']

    def parse(self, response):
        pass
