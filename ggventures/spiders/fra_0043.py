import scrapy


class Fra0043Spider(scrapy.Spider):
    name = 'fra_0043'
    allowed_domains = ['https://seg.univ-lyon2.fr/']
    start_urls = ['http://https://seg.univ-lyon2.fr//']

    def parse(self, response):
        pass
