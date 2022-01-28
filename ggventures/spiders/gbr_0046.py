import scrapy


class Gbr0046Spider(scrapy.Spider):
    name = 'gbr_0046'
    allowed_domains = ['https://www.surrey.ac.uk/business-school']
    start_urls = ['http://https://www.surrey.ac.uk/business-school/']

    def parse(self, response):
        pass
