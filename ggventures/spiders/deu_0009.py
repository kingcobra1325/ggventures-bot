import scrapy


class Deu0009Spider(scrapy.Spider):
    name = 'deu_0009'
    allowed_domains = ['https://www.frankfurt-school.de/home']
    start_urls = ['http://https://www.frankfurt-school.de/home/']

    def parse(self, response):
        pass
