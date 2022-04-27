import scrapy


class Bra0012Spider(scrapy.Spider):
    name = 'bra_0012'
    allowed_domains = ['https://www.face.ufmg.br/institucional/quem-somos.html']
    start_urls = ['http://https://www.face.ufmg.br/institucional/quem-somos.html/']

    def parse(self, response):
        pass
