import scrapy


class Ita0012Spider(scrapy.Spider):
    name = 'ita_0012'
    allowed_domains = ['https://www.sdabocconi.it/en/home']
    start_urls = ['http://https://www.sdabocconi.it/en/home/']

    def parse(self, response):
        pass
