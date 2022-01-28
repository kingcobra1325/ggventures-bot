import scrapy


class Gbr0043Spider(scrapy.Spider):
    name = 'gbr_0043'
    allowed_domains = ['https://www.southampton.ac.uk/business-school/index.page']
    start_urls = ['http://https://www.southampton.ac.uk/business-school/index.page/']

    def parse(self, response):
        pass
