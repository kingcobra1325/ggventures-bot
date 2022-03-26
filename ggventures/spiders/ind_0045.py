import scrapy


class Ind0045Spider(scrapy.Spider):
    name = 'ind_0045'
    allowed_domains = ['http://www.iipm.edu/']
    start_urls = ['http://http://www.iipm.edu//']

    def parse(self, response):
        pass
