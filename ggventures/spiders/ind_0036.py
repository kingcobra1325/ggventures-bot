import scrapy


class Ind0036Spider(scrapy.Spider):
    name = 'ind_0036'
    allowed_domains = ['http://prestigegwl.org/']
    start_urls = ['http://http://prestigegwl.org//']

    def parse(self, response):
        pass
