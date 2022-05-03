import scrapy


class Esp0011Spider(scrapy.Spider):
    name = 'esp_0011'
    allowed_domains = ['https://www.esic.edu/']
    start_urls = ['http://https://www.esic.edu//']

    def parse(self, response):
        pass
