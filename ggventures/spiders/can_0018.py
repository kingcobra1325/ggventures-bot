import scrapy


class Can0018Spider(scrapy.Spider):
    name = 'can_0018'
    allowed_domains = ['https://umanitoba.ca/asper/']
    start_urls = ['http://https://umanitoba.ca/asper//']

    def parse(self, response):
        pass
