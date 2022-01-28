import scrapy


class Gbr0042Spider(scrapy.Spider):
    name = 'gbr_0042'
    allowed_domains = ['https://www.plymouth.ac.uk/schools/plymouth-business-school']
    start_urls = ['http://https://www.plymouth.ac.uk/schools/plymouth-business-school/']

    def parse(self, response):
        pass
