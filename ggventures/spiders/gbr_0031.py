import scrapy


class Gbr0031Spider(scrapy.Spider):
    name = 'gbr_0031'
    allowed_domains = ['https://www.birmingham.ac.uk/schools/business/index.aspx']
    start_urls = ['http://https://www.birmingham.ac.uk/schools/business/index.aspx/']

    def parse(self, response):
        pass
