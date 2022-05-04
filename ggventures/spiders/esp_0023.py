import scrapy


class Esp0023Spider(scrapy.Spider):
    name = 'esp_0023'
    allowed_domains = ['https://www.unav.edu/web/facultad-de-ciencias-economicas-y-empresariales']
    start_urls = ['http://https://www.unav.edu/web/facultad-de-ciencias-economicas-y-empresariales/']

    def parse(self, response):
        pass
