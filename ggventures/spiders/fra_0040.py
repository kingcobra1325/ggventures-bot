import scrapy


class Fra0040Spider(scrapy.Spider):
    name = 'fra_0040'
    allowed_domains = ['https://iae.univ-poitiers.fr/en/7896-2/']
    start_urls = ['http://https://iae.univ-poitiers.fr/en/7896-2//']

    def parse(self, response):
        pass
