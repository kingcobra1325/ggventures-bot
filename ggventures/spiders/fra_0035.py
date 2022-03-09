import scrapy


class Fra0035Spider(scrapy.Spider):
    name = 'fra_0035'
    allowed_domains = ['http://www.reims-ms.fr/en/groupe/']
    start_urls = ['http://http://www.reims-ms.fr/en/groupe//']

    def parse(self, response):
        pass
