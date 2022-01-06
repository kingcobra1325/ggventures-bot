import scrapy


class Usa0044Spider(scrapy.Spider):
    name = 'usa_0044'
    allowed_domains = ['https://www.luc.edu/quinlan/']
    start_urls = ['http://https://www.luc.edu/quinlan//']

    def parse(self, response):
        pass
