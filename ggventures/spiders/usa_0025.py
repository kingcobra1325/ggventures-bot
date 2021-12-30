import scrapy


class Usa0025Spider(scrapy.Spider):
    name = 'usa_0025'
    allowed_domains = ['https://www.fuqua.duke.edu/']
    start_urls = ['http://https://www.fuqua.duke.edu//']

    def parse(self, response):
        pass
