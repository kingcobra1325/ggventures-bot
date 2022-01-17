import scrapy


class Usa0138Spider(scrapy.Spider):
    name = 'usa_0138'
    allowed_domains = ['https://www.utoledo.edu/business']
    start_urls = ['http://https://www.utoledo.edu/business/']

    def parse(self, response):
        pass
