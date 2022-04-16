import scrapy


class Pol0007Spider(scrapy.Spider):
    name = 'pol_0007'
    allowed_domains = ['https://www.sgh.waw.pl/en/Pages/default.aspx']
    start_urls = ['http://https://www.sgh.waw.pl/en/Pages/default.aspx/']

    def parse(self, response):
        pass
