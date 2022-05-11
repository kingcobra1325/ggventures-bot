import scrapy


class Tur0002Spider(scrapy.Spider):
    name = 'tur_0002'
    allowed_domains = ['https://www.emu.edu.tr/en/academics/faculties/faculty-of-business-economics/700']
    start_urls = ['http://https://www.emu.edu.tr/en/academics/faculties/faculty-of-business-economics/700/']

    def parse(self, response):
        pass
