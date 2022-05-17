import scrapy


class Rus0012Spider(scrapy.Spider):
    name = 'rus_0012'
    allowed_domains = ['http://en.mgubs.ru/']
    start_urls = ['http://http://en.mgubs.ru//']

    def parse(self, response):
        pass
