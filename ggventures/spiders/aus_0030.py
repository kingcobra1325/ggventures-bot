import scrapy


class Aus0030Spider(scrapy.Spider):
    name = 'aus_0030'
    allowed_domains = ['https://www.uts.edu.au/about/uts-business-school']
    start_urls = ['http://https://www.uts.edu.au/about/uts-business-school/']

    def parse(self, response):
        pass
