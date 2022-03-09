import scrapy


class Fra0038Spider(scrapy.Spider):
    name = 'fra_0038'
    allowed_domains = ['https://www.montpellier-bs.com/international/']
    start_urls = ['http://https://www.montpellier-bs.com/international//']

    def parse(self, response):
        pass
