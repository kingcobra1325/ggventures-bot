import scrapy


class Esp0005Spider(scrapy.Spider):
    name = 'esp_0005'
    allowed_domains = ['https://een.edu/']
    start_urls = ['http://https://een.edu//']

    def parse(self, response):
        pass
