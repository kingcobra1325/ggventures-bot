import scrapy


class Esp0006Spider(scrapy.Spider):
    name = 'esp_0006'
    allowed_domains = ['https://www.eoi.es/es']
    start_urls = ['http://https://www.eoi.es/es/']

    def parse(self, response):
        pass
