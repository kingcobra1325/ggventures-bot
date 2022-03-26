import scrapy


class Ind0042Spider(scrapy.Spider):
    name = 'ind_0042'
    allowed_domains = ['https://www.sibm.edu/']
    start_urls = ['http://https://www.sibm.edu//']

    def parse(self, response):
        pass
