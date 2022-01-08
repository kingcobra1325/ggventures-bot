import scrapy


class Usa0063Spider(scrapy.Spider):
    name = 'usa_0063'
    allowed_domains = ['https://www.slu.edu/business/index.php']
    start_urls = ['http://https://www.slu.edu/business/index.php/']

    def parse(self, response):
        pass
