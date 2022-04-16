import scrapy


class Pol0008Spider(scrapy.Spider):
    name = 'pol_0008'
    allowed_domains = ['https://ue.poznan.pl/en/']
    start_urls = ['http://https://ue.poznan.pl/en//']

    def parse(self, response):
        pass
