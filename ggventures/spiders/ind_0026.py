import scrapy


class Ind0026Spider(scrapy.Spider):
    name = 'ind_0026'
    allowed_domains = ['https://imi-luzern.com/']
    start_urls = ['http://https://imi-luzern.com//']

    def parse(self, response):
        pass
