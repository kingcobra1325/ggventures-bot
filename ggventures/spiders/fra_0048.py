import scrapy


class Fra0048Spider(scrapy.Spider):
    name = 'fra_0048'
    allowed_domains = ['https://dauphine.psl.eu/en/']
    start_urls = ['http://https://dauphine.psl.eu/en//']

    def parse(self, response):
        pass
