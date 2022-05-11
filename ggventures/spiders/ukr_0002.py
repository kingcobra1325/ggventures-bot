import scrapy


class Ukr0002Spider(scrapy.Spider):
    name = 'ukr_0002'
    allowed_domains = ['https://mim.kyiv.ua/en']
    start_urls = ['http://https://mim.kyiv.ua/en/']

    def parse(self, response):
        pass
