import scrapy


class Tha0006Spider(scrapy.Spider):
    name = 'tha_0006'
    allowed_domains = ['https://www.fms.psu.ac.th/?lang=en']
    start_urls = ['http://https://www.fms.psu.ac.th/?lang=en/']

    def parse(self, response):
        pass
