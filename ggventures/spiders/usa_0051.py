import scrapy


class Usa0051Spider(scrapy.Spider):
    name = 'usa_0051'
    allowed_domains = ['https://www.stern.nyu.edu/']
    start_urls = ['http://https://www.stern.nyu.edu//']

    def parse(self, response):
        pass
