import scrapy


class Gbr0016Spider(scrapy.Spider):
    name = 'gbr_0016'
    allowed_domains = ['https://www.london.edu/']
    start_urls = ['http://https://www.london.edu//']

    def parse(self, response):
        pass
