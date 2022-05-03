import scrapy


class Esp0014Spider(scrapy.Spider):
    name = 'esp_0014'
    allowed_domains = ['https://www.ie.edu/business-school/']
    start_urls = ['http://https://www.ie.edu/business-school//']

    def parse(self, response):
        pass
