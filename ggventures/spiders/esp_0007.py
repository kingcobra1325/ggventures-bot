import scrapy


class Esp0007Spider(scrapy.Spider):
    name = 'esp_0007'
    allowed_domains = ['https://www.esade.edu/en']
    start_urls = ['http://https://www.esade.edu/en/']

    def parse(self, response):
        pass
