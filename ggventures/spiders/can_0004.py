import scrapy


class Can0004Spider(scrapy.Spider):
    name = 'can_0004'
    allowed_domains = ['https://www.dal.ca/']
    start_urls = ['http://https://www.dal.ca//']

    def parse(self, response):
        pass
