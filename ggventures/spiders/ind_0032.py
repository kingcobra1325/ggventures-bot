import scrapy


class Ind0032Spider(scrapy.Spider):
    name = 'ind_0032'
    allowed_domains = ['https://www.nmims.edu/']
    start_urls = ['http://https://www.nmims.edu//']

    def parse(self, response):
        pass
