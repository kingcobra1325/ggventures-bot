import scrapy


class Fra0024Spider(scrapy.Spider):
    name = 'fra_0024'
    allowed_domains = ['http://www.essec.edu/en/']
    start_urls = ['http://http://www.essec.edu/en//']

    def parse(self, response):
        pass
