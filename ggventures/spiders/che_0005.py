import scrapy


class Che0005Spider(scrapy.Spider):
    name = 'che_0005'
    allowed_domains = ['https://www.iun.ch/en-en']
    start_urls = ['http://https://www.iun.ch/en-en/']

    def parse(self, response):
        pass
