import scrapy


class Usa0112Spider(scrapy.Spider):
    name = 'usa_0112'
    allowed_domains = ['https://www.terry.uga.edu/']
    start_urls = ['http://https://www.terry.uga.edu//']

    def parse(self, response):
        pass
