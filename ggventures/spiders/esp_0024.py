import scrapy


class Esp0024Spider(scrapy.Spider):
    name = 'esp_0024'
    allowed_domains = ['https://www.comillas.edu/en/']
    start_urls = ['http://https://www.comillas.edu/en//']

    def parse(self, response):
        pass
