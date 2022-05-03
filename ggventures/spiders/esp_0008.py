import scrapy


class Esp0008Spider(scrapy.Spider):
    name = 'esp_0008'
    allowed_domains = ['https://www.escp.eu/madrid']
    start_urls = ['http://https://www.escp.eu/madrid/']

    def parse(self, response):
        pass
