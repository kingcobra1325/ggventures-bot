import scrapy


class Deu0026Spider(scrapy.Spider):
    name = 'deu_0026'
    allowed_domains = ['https://www.uni-kiel.de/en/university/facilities-faculties/faculties-joint-facilities/faculty-of-business-economics-and-social-sciences']
    start_urls = ['http://https://www.uni-kiel.de/en/university/facilities-faculties/faculties-joint-facilities/faculty-of-business-economics-and-social-sciences/']

    def parse(self, response):
        pass
