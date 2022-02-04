import scrapy


class Aus0007Spider(scrapy.Spider):
    name = 'aus_0007'
    allowed_domains = ['https://www.ecu.edu.au/schools/business-and-law']
    start_urls = ['http://https://www.ecu.edu.au/schools/business-and-law/']

    def parse(self, response):
        pass
