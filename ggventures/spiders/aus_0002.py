import scrapy


class Aus0002Spider(scrapy.Spider):
    name = 'aus_0002'
    allowed_domains = ['https://bond.edu.au/intl/about-bond/academia/bond-business-school']
    start_urls = ['http://https://bond.edu.au/intl/about-bond/academia/bond-business-school/']

    def parse(self, response):
        pass
