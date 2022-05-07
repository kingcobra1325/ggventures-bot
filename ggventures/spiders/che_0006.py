import scrapy


class Che0006Spider(scrapy.Spider):
    name = 'che_0006'
    allowed_domains = ['https://mtec.ethz.ch/']
    start_urls = ['http://https://mtec.ethz.ch//']

    def parse(self, response):
        pass
