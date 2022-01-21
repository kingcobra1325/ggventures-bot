import scrapy


class Gbr0017Spider(scrapy.Spider):
    name = 'gbr_0017'
    allowed_domains = ['https://www.lboro.ac.uk/departments/sbe/']
    start_urls = ['http://https://www.lboro.ac.uk/departments/sbe//']

    def parse(self, response):
        pass
