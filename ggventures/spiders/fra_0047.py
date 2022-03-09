import scrapy


class Fra0047Spider(scrapy.Spider):
    name = 'fra_0047'
    allowed_domains = ['https://www.u-paris2.fr/en']
    start_urls = ['http://https://www.u-paris2.fr/en/']

    def parse(self, response):
        pass
