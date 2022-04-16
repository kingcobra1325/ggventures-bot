import scrapy


class Pol0009Spider(scrapy.Spider):
    name = 'pol_0009'
    allowed_domains = ['https://en.uw.edu.pl/tag/faculty-of-management/']
    start_urls = ['http://https://en.uw.edu.pl/tag/faculty-of-management//']

    def parse(self, response):
        pass
