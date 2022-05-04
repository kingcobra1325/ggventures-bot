import scrapy


class Esp0025Spider(scrapy.Spider):
    name = 'esp_0025'
    allowed_domains = ['https://www.upf.edu/en/']
    start_urls = ['http://https://www.upf.edu/en//']

    def parse(self, response):
        pass
