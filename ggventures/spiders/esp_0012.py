import scrapy


class Esp0012Spider(scrapy.Spider):
    name = 'esp_0012'
    allowed_domains = ['http://www.foroeuropeo.com/']
    start_urls = ['http://http://www.foroeuropeo.com//']

    def parse(self, response):
        pass
