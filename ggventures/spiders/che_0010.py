import scrapy


class Che0010Spider(scrapy.Spider):
    name = 'che_0010'
    allowed_domains = ['https://www.unil.ch/hec/en/home.html']
    start_urls = ['http://https://www.unil.ch/hec/en/home.html/']

    def parse(self, response):
        pass
