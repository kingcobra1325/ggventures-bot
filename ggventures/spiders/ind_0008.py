import scrapy


class Ind0008Spider(scrapy.Spider):
    name = 'ind_0008'
    allowed_domains = ['https://www.fsm.ac.in/']
    start_urls = ['http://https://www.fsm.ac.in//']

    def parse(self, response):
        pass
