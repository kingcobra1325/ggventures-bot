import scrapy


class Can0015Spider(scrapy.Spider):
    name = 'can_0015'
    allowed_domains = ['https://www.ualberta.ca/business/index.html']
    start_urls = ['http://https://www.ualberta.ca/business/index.html/']

    def parse(self, response):
        pass
