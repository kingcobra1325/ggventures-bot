import scrapy


class Usa0150Spider(scrapy.Spider):
    name = 'usa_0150'
    allowed_domains = ['https://olin.wustl.edu/']
    start_urls = ['http://https://olin.wustl.edu//']

    def parse(self, response):
        pass
