import scrapy


class Esp0018Spider(scrapy.Spider):
    name = 'esp_0018'
    allowed_domains = ['https://www.salleurl.edu/en']
    start_urls = ['http://https://www.salleurl.edu/en/']

    def parse(self, response):
        pass
