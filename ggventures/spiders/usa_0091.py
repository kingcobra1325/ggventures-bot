import scrapy


class Usa0091Spider(scrapy.Spider):
    name = 'usa_0091'
    allowed_domains = ['https://www.mccombs.utexas.edu/']
    start_urls = ['http://https://www.mccombs.utexas.edu//']

    def parse(self, response):
        pass
