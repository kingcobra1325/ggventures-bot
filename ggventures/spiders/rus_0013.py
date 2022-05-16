import scrapy


class Rus0013Spider(scrapy.Spider):
    name = 'rus_0013'
    allowed_domains = ['https://pstu.ru/en/']
    start_urls = ['http://https://pstu.ru/en//']

    def parse(self, response):
        pass
