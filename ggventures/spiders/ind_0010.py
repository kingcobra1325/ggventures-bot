import scrapy


class Ind0010Spider(scrapy.Spider):
    name = 'ind_0010'
    allowed_domains = ['https://www.icfaiuniversity.in/']
    start_urls = ['http://https://www.icfaiuniversity.in//']

    def parse(self, response):
        pass
