import scrapy


class Fra0023Spider(scrapy.Spider):
    name = 'fra_0023'
    allowed_domains = ['https://www.essca.fr/en/']
    start_urls = ['http://https://www.essca.fr/en//']

    def parse(self, response):
        pass
