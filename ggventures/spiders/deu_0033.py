import scrapy


class Deu0033Spider(scrapy.Spider):
    name = 'deu_0033'
    allowed_domains = ['https://www.uni-wh.de/en/uwh-international/university/faculty-of-management-economics-and-society/']
    start_urls = ['http://https://www.uni-wh.de/en/uwh-international/university/faculty-of-management-economics-and-society//']

    def parse(self, response):
        pass
