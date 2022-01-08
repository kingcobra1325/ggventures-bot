import scrapy


class Usa0085Spider(scrapy.Spider):
    name = 'usa_0085'
    allowed_domains = ['https://www.kenan-flagler.unc.edu/']
    start_urls = ['http://https://www.kenan-flagler.unc.edu//']

    def parse(self, response):
        pass
