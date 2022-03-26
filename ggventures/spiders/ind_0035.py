import scrapy


class Ind0035Spider(scrapy.Spider):
    name = 'ind_0035'
    allowed_domains = ['https://science.nirmauni.ac.in/']
    start_urls = ['http://https://science.nirmauni.ac.in//']

    def parse(self, response):
        pass
