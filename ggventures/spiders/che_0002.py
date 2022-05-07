import scrapy


class Che0002Spider(scrapy.Spider):
    name = 'che_0002'
    allowed_domains = ['https://www.gsb.uzh.ch/en.html']
    start_urls = ['http://https://www.gsb.uzh.ch/en.html/']

    def parse(self, response):
        pass
