import scrapy


class Deu0021Spider(scrapy.Spider):
    name = 'deu_0021'
    allowed_domains = ['https://www.rw.fau.eu/faculty/school-of-business-and-economics/']
    start_urls = ['http://https://www.rw.fau.eu/faculty/school-of-business-and-economics//']

    def parse(self, response):
        pass
