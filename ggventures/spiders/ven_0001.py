import scrapy


class Ven0001Spider(scrapy.Spider):
    name = 'ven_0001'
    allowed_domains = ['http://www.iesa.edu.ve/english']
    start_urls = ['http://http://www.iesa.edu.ve/english/']

    def parse(self, response):
        pass
