import scrapy


class Usa0019Spider(scrapy.Spider):
    name = 'usa_0019'
    allowed_domains = ['https://home.gsb.columbia.edu/']
    start_urls = ['http://https://home.gsb.columbia.edu//']

    def parse(self, response):
        pass
