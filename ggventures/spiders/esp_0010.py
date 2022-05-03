import scrapy


class Esp0010Spider(scrapy.Spider):
    name = 'esp_0010'
    allowed_domains = ['https://www.eseune.edu/']
    start_urls = ['http://https://www.eseune.edu//']

    def parse(self, response):
        pass
