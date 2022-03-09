import scrapy


class Fra0049Spider(scrapy.Spider):
    name = 'fra_0049'
    allowed_domains = ['https://www.grenoble-iae.fr/']
    start_urls = ['http://https://www.grenoble-iae.fr//']

    def parse(self, response):
        pass
