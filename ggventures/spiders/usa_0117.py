import scrapy


class Usa0117Spider(scrapy.Spider):
    name = 'usa_0117'
    allowed_domains = ['https://business.louisville.edu/academics-programs/graduate-programs/']
    start_urls = ['http://https://business.louisville.edu/academics-programs/graduate-programs//']

    def parse(self, response):
        pass
