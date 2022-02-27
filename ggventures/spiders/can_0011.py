import scrapy


class Can0011Spider(scrapy.Spider):
    name = 'can_0011'
    allowed_domains = ['https://beedie.sfu.ca/']
    start_urls = ['http://https://beedie.sfu.ca//']

    def parse(self, response):
        pass
