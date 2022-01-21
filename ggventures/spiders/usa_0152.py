import scrapy


class Usa0152Spider(scrapy.Spider):
    name = 'usa_0152'
    allowed_domains = ['https://www.wpi.edu/academics/business/faculty']
    start_urls = ['http://https://www.wpi.edu/academics/business/faculty/']

    def parse(self, response):
        pass
