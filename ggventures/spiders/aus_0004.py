import scrapy


class Aus0004Spider(scrapy.Spider):
    name = 'aus_0004'
    allowed_domains = ['https://www.cdu.edu.au/business-law']
    start_urls = ['http://https://www.cdu.edu.au/business-law/']

    def parse(self, response):
        pass
