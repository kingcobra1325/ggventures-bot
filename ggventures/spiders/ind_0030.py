import scrapy


class Ind0030Spider(scrapy.Spider):
    name = 'ind_0030'
    allowed_domains = ['https://liba.edu/']
    start_urls = ['http://https://liba.edu//']

    def parse(self, response):
        pass
