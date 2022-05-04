import scrapy


class Esp0009Spider(scrapy.Spider):
    name = 'esp_0009'
    allowed_domains = ['https://es.eserp.com/conoce-eserp/fundacion/conoce-la-fundacion-universitaria/']
    start_urls = ['http://https://es.eserp.com/conoce-eserp/fundacion/conoce-la-fundacion-universitaria//']

    def parse(self, response):
        pass
