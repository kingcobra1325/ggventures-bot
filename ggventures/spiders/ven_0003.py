import scrapy


class Ven0003Spider(scrapy.Spider):
    name = 'ven_0003'
    allowed_domains = ['http://www.ula.ve/ciencias-economicas-sociales/']
    start_urls = ['http://http://www.ula.ve/ciencias-economicas-sociales//']

    def parse(self, response):
        pass
