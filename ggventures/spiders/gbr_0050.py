import scrapy


class Gbr0050Spider(scrapy.Spider):
    name = 'gbr_0050'
    allowed_domains = ['https://www.wbs.ac.uk/']
    start_urls = ['http://https://www.wbs.ac.uk//']

    def parse(self, response):
        pass
