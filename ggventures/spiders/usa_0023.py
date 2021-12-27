import scrapy


class Usa0023Spider(scrapy.Spider):
    name = 'usa_0023'
    allowed_domains = ['https://business.depaul.edu/Pages/default.aspx']
    start_urls = ['http://https://business.depaul.edu/Pages/default.aspx/']

    def parse(self, response):
        pass
