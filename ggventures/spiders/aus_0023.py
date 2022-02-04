import scrapy


class Aus0023Spider(scrapy.Spider):
    name = 'aus_0023'
    allowed_domains = ['https://federation.edu.au/schools/federation-business-school']
    start_urls = ['http://https://federation.edu.au/schools/federation-business-school/']

    def parse(self, response):
        pass
