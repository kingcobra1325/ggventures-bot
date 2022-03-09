import scrapy


class Fra0021Spider(scrapy.Spider):
    name = 'fra_0021'
    allowed_domains = ['https://www.esg.fr/ecole-paris']
    start_urls = ['http://https://www.esg.fr/ecole-paris/']

    def parse(self, response):
        pass
