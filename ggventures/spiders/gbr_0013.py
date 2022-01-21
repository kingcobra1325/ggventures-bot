import scrapy


class Gbr0013Spider(scrapy.Spider):
    name = 'gbr_0013'
    allowed_domains = ['https://www.imperial.ac.uk/business-school/']
    start_urls = ['http://https://www.imperial.ac.uk/business-school//']

    def parse(self, response):
        pass
