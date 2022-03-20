import scrapy


class Deu0035Spider(scrapy.Spider):
    name = 'deu_0035'
    allowed_domains = ['https://www.whu.edu/en/']
    start_urls = ['http://https://www.whu.edu/en//']

    def parse(self, response):
        pass
