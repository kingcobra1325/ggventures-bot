import scrapy


class Fra0041Spider(scrapy.Spider):
    name = 'fra_0041'
    allowed_domains = ['https://economie.uca.fr/']
    start_urls = ['http://https://economie.uca.fr//']

    def parse(self, response):
        pass
