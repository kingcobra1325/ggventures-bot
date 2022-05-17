import scrapy


class Rus0015Spider(scrapy.Spider):
    name = 'rus_0015'
    allowed_domains = ['https://gsom.spbu.ru/en/']
    start_urls = ['http://https://gsom.spbu.ru/en//']

    def parse(self, response):
        pass
