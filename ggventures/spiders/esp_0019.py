import scrapy


class Esp0019Spider(scrapy.Spider):
    name = 'esp_0019'
    allowed_domains = ['https://business.uc3m.es/']
    start_urls = ['http://https://business.uc3m.es//']

    def parse(self, response):
        pass
