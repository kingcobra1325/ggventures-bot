import scrapy


class Usa0086Spider(scrapy.Spider):
    name = 'usa_0086'
    allowed_domains = ['https://belkcollege.charlotte.edu/']
    start_urls = ['http://https://belkcollege.charlotte.edu//']

    def parse(self, response):
        pass
