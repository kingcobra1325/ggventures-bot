import scrapy


class Ind0020Spider(scrapy.Spider):
    name = 'ind_0020'
    allowed_domains = ['https://www.isb.edu/en.html']
    start_urls = ['http://https://www.isb.edu/en.html/']

    def parse(self, response):
        pass
