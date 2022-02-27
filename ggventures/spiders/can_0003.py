import scrapy


class Can0003Spider(scrapy.Spider):
    name = 'can_0003'
    allowed_domains = ['https://www.concordia.ca/jmsb.html']
    start_urls = ['http://https://www.concordia.ca/jmsb.html/']

    def parse(self, response):
        pass
