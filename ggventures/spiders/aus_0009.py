import scrapy


class Aus0009Spider(scrapy.Spider):
    name = 'aus_0009'
    allowed_domains = ['https://www.jcu.edu.au/college-of-business-law-and-governance']
    start_urls = ['http://https://www.jcu.edu.au/college-of-business-law-and-governance/']

    def parse(self, response):
        pass
