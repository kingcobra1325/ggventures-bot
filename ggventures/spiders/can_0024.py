import scrapy


class Can0024Spider(scrapy.Spider):
    name = 'can_0024'
    allowed_domains = ['https://www.ivey.uwo.ca/']
    start_urls = ['http://https://www.ivey.uwo.ca//']

    def parse(self, response):
        pass
