import scrapy


class Ind0021Spider(scrapy.Spider):
    name = 'ind_0021'
    allowed_domains = ['https://www.iofm.com/']
    start_urls = ['http://https://www.iofm.com//']

    def parse(self, response):
        pass
