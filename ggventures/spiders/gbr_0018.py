import scrapy


class Gbr0018Spider(scrapy.Spider):
    name = 'gbr_0018'
    allowed_domains = ['https://www.lse.ac.uk/']
    start_urls = ['http://https://www.lse.ac.uk//']

    def parse(self, response):
        pass
