import scrapy


class Gbr0041Spider(scrapy.Spider):
    name = 'gbr_0041'
    allowed_domains = ['https://www.sbs.ox.ac.uk/']
    start_urls = ['http://https://www.sbs.ox.ac.uk//']

    def parse(self, response):
        pass
