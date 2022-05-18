import scrapy


class Ven0002Spider(scrapy.Spider):
    name = 'ven_0002'
    allowed_domains = ['http://www.ucv.ve/estructura/facultades/facultad-de-ciencias-economicas-y-sociales.html']
    start_urls = ['http://http://www.ucv.ve/estructura/facultades/facultad-de-ciencias-economicas-y-sociales.html/']

    def parse(self, response):
        pass
