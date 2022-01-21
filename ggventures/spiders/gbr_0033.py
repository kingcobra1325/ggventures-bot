import scrapy


class Gbr0033Spider(scrapy.Spider):
    name = 'gbr_0033'
    allowed_domains = ['https://www.dur.ac.uk/business/']
    start_urls = ['http://https://www.dur.ac.uk/business//']

    def parse(self, response):
        pass
