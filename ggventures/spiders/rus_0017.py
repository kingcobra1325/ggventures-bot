import scrapy


class Rus0017Spider(scrapy.Spider):
    name = 'rus_0017'
    allowed_domains = ['https://guu.ru/language/en/']
    start_urls = ['http://https://guu.ru/language/en//']

    def parse(self, response):
        pass
