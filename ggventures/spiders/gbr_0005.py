import scrapy


class Gbr0005Spider(scrapy.Spider):
    name = 'gbr_0005'
    allowed_domains = ['https://www.brunel.ac.uk/business-school']
    start_urls = ['http://https://www.brunel.ac.uk/business-school/']

    def parse(self, response):
        pass
