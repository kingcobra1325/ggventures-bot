import scrapy


class Aus0008Spider(scrapy.Spider):
    name = 'aus_0008'
    allowed_domains = ['https://www.griffith.edu.au/griffith-business-school']
    start_urls = ['http://https://www.griffith.edu.au/griffith-business-school/']

    def parse(self, response):
        pass
