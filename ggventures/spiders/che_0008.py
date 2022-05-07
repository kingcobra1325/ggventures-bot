import scrapy


class Che0008Spider(scrapy.Spider):
    name = 'che_0008'
    allowed_domains = ['https://www.unisg.ch/en']
    start_urls = ['http://https://www.unisg.ch/en/']

    def parse(self, response):
        pass
