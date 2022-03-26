import scrapy


class Ind0041Spider(scrapy.Spider):
    name = 'ind_0041'
    allowed_domains = ['https://www.scmhrd.edu/']
    start_urls = ['http://https://www.scmhrd.edu//']

    def parse(self, response):
        pass
