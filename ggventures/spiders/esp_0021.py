import scrapy


class Esp0021Spider(scrapy.Spider):
    name = 'esp_0021'
    allowed_domains = ['https://www.ucm.es/']
    start_urls = ['http://https://www.ucm.es//']

    def parse(self, response):
        pass
