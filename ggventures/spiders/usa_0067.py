import scrapy


class Usa0067Spider(scrapy.Spider):
    name = 'usa_0067'
    allowed_domains = ['https://www.smu.edu/cox']
    start_urls = ['http://https://www.smu.edu/cox/']

    def parse(self, response):
        pass
