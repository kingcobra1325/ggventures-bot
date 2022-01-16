import scrapy


class Usa0137Spider(scrapy.Spider):
    name = 'usa_0137'
    allowed_domains = ['https://haslam.utk.edu/']
    start_urls = ['http://https://haslam.utk.edu//']

    def parse(self, response):
        pass
