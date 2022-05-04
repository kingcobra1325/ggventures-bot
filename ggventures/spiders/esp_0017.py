import scrapy


class Esp0017Spider(scrapy.Spider):
    name = 'esp_0017'
    allowed_domains = ['https://www.santelmo.org/']
    start_urls = ['http://https://www.santelmo.org//']

    def parse(self, response):
        pass
