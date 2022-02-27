import scrapy


class Can0026Spider(scrapy.Spider):
    name = 'can_0026'
    allowed_domains = ['https://schulich.yorku.ca/']
    start_urls = ['http://https://schulich.yorku.ca//']

    def parse(self, response):
        pass
