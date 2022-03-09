import scrapy


class Fra0032Spider(scrapy.Spider):
    name = 'fra_0032'
    allowed_domains = ['https://www.imt-bs.eu/en/']
    start_urls = ['http://https://www.imt-bs.eu/en//']

    def parse(self, response):
        pass
