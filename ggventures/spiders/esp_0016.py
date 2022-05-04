import scrapy


class Esp0016Spider(scrapy.Spider):
    name = 'esp_0016'
    allowed_domains = ['https://www.iese.edu/']
    start_urls = ['http://https://www.iese.edu//']

    def parse(self, response):
        pass
