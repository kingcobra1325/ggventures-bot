import scrapy


class Ind0007Spider(scrapy.Spider):
    name = 'ind_0007'
    allowed_domains = ['https://christuniversity.in/']
    start_urls = ['http://https://christuniversity.in//']

    def parse(self, response):
        pass
