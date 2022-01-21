import scrapy


class Gbr0029Spider(scrapy.Spider):
    name = 'gbr_0029'
    allowed_domains = ['https://www.gla.ac.uk/schools/business/']
    start_urls = ['http://https://www.gla.ac.uk/schools/business//']

    def parse(self, response):
        pass
