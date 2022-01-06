import scrapy


class Usa0052Spider(scrapy.Spider):
    name = 'usa_0052'
    allowed_domains = ['https://damore-mckim.northeastern.edu/']
    start_urls = ['http://https://damore-mckim.northeastern.edu//']

    def parse(self, response):
        pass
