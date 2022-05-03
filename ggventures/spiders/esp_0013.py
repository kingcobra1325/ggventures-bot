import scrapy


class Esp0013Spider(scrapy.Spider):
    name = 'esp_0013'
    allowed_domains = ['https://www.fundesem.es/']
    start_urls = ['http://https://www.fundesem.es//']

    def parse(self, response):
        pass
