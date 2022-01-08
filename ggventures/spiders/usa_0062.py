import scrapy


class Usa0062Spider(scrapy.Spider):
    name = 'usa_0062'
    allowed_domains = ['https://www.sju.edu/haub-school-business']
    start_urls = ['http://https://www.sju.edu/haub-school-business/']

    def parse(self, response):
        pass
