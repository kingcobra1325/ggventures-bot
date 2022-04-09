import scrapy


class Ita0018Spider(scrapy.Spider):
    name = 'ita_0018'
    allowed_domains = ['https://www.unito.it/ugov/degree/38271']
    start_urls = ['http://https://www.unito.it/ugov/degree/38271/']

    def parse(self, response):
        pass
