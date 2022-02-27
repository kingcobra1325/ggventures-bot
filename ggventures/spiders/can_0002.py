import scrapy


class Can0002Spider(scrapy.Spider):
    name = 'can_0002'
    allowed_domains = ['https://sprott.carleton.ca/']
    start_urls = ['http://https://sprott.carleton.ca//']

    def parse(self, response):
        pass
