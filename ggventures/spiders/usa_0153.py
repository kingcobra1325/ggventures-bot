import scrapy


class Usa0153Spider(scrapy.Spider):
    name = 'usa_0153'
    allowed_domains = ['https://www.xavier.edu/williams/']
    start_urls = ['http://https://www.xavier.edu/williams//']

    def parse(self, response):
        pass
