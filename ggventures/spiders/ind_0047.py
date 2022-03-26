import scrapy


class Ind0047Spider(scrapy.Spider):
    name = 'ind_0047'
    allowed_domains = ['http://www.du.ac.in/']
    start_urls = ['http://http://www.du.ac.in//']

    def parse(self, response):
        pass
