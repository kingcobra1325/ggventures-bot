import scrapy


class Rus0016Spider(scrapy.Spider):
    name = 'rus_0016'
    allowed_domains = ['https://www.hse.ru/en/education/']
    start_urls = ['http://https://www.hse.ru/en/education//']

    def parse(self, response):
        pass
