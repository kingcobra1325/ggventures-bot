import scrapy


class Rus0011Spider(scrapy.Spider):
    name = 'rus_0011'
    allowed_domains = ['https://eng.mirbis.ru/']
    start_urls = ['http://https://eng.mirbis.ru//']

    def parse(self, response):
        pass
