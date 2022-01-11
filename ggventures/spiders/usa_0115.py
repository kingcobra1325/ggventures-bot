import scrapy


class Usa0115Spider(scrapy.Spider):
    name = 'usa_0115'
    allowed_domains = ['https://giesbusiness.illinois.edu/']
    start_urls = ['http://https://giesbusiness.illinois.edu//']

    def parse(self, response):
        pass
