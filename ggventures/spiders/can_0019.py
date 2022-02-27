import scrapy


class Can0019Spider(scrapy.Spider):
    name = 'can_0019'
    allowed_domains = ['https://www.unb.ca/']
    start_urls = ['http://https://www.unb.ca//']

    def parse(self, response):
        pass
