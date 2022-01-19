import scrapy


class Gbr0002Spider(scrapy.Spider):
    name = 'gbr_0002'
    allowed_domains = ['https://www.hult.edu/en/ashridge/']
    start_urls = ['http://https://www.hult.edu/en/ashridge//']

    def parse(self, response):
        pass
