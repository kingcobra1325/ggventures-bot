import scrapy


class Usa0141Spider(scrapy.Spider):
    name = 'usa_0141'
    allowed_domains = ['https://www.darden.virginia.edu/']
    start_urls = ['http://https://www.darden.virginia.edu//']

    def parse(self, response):
        pass
