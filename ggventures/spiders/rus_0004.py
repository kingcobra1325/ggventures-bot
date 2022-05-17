import scrapy


class Rus0004Spider(scrapy.Spider):
    name = 'rus_0004'
    allowed_domains = ['https://imisp.ru/en/']
    start_urls = ['http://https://imisp.ru/en//']

    def parse(self, response):
        pass
