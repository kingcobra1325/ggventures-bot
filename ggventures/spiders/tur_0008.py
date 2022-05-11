import scrapy


class Tur0008Spider(scrapy.Spider):
    name = 'tur_0008'
    allowed_domains = ['https://sbs.sabanciuniv.edu/en']
    start_urls = ['http://https://sbs.sabanciuniv.edu/en/']

    def parse(self, response):
        pass
