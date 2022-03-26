import scrapy


class Ind0028Spider(scrapy.Spider):
    name = 'ind_0028'
    allowed_domains = ['https://simsr.somaiya.edu/']
    start_urls = ['http://https://simsr.somaiya.edu//']

    def parse(self, response):
        pass
