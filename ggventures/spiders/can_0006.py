import scrapy


class Can0006Spider(scrapy.Spider):
    name = 'can_0006'
    allowed_domains = ['https://www.mcgill.ca/desautels/']
    start_urls = ['http://https://www.mcgill.ca/desautels//']

    def parse(self, response):
        pass
