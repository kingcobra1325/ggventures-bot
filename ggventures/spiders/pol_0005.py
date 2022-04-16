import scrapy


class Pol0005Spider(scrapy.Spider):
    name = 'pol_0005'
    allowed_domains = ['https://www.econ.umk.pl/en/']
    start_urls = ['http://https://www.econ.umk.pl/en//']

    def parse(self, response):
        pass
