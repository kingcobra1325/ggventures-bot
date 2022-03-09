import scrapy


class Fra0029Spider(scrapy.Spider):
    name = 'fra_0029'
    allowed_domains = ['https://www.ieseg.fr/en/']
    start_urls = ['http://https://www.ieseg.fr/en//']

    def parse(self, response):
        pass
