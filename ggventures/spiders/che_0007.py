import scrapy


class Che0007Spider(scrapy.Spider):
    name = 'che_0007'
    allowed_domains = ['https://www.investopedia.com/terms/e/economics.asp']
    start_urls = ['http://https://www.investopedia.com/terms/e/economics.asp/']

    def parse(self, response):
        pass
