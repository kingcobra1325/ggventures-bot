import scrapy


class Ind0037Spider(scrapy.Spider):
    name = 'ind_0037'
    allowed_domains = ['https://www.welingkar.org/']
    start_urls = ['http://https://www.welingkar.org//']

    def parse(self, response):
        pass
