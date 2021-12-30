import scrapy


class Usa0028Spider(scrapy.Spider):
    name = 'usa_0028'
    allowed_domains = ['https://www.fdu.edu/academics/colleges-schools/silberman/']
    start_urls = ['http://https://www.fdu.edu/academics/colleges-schools/silberman//']

    def parse(self, response):
        pass
