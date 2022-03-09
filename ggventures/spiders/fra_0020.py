import scrapy


class Fra0020Spider(scrapy.Spider):
    name = 'fra_0020'
    allowed_domains = ['https://www.esdes.fr/en/']
    start_urls = ['http://https://www.esdes.fr/en//']

    def parse(self, response):
        pass
