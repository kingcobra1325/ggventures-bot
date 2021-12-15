import scrapy


class Usa0008Spider(scrapy.Spider):
    name = 'usa-0008'
    allowed_domains = ['https://www.bc.edu/bc-web/schools/carroll-school.html']
    start_urls = ['http://https://www.bc.edu/bc-web/schools/carroll-school.html/']

    def parse(self, response):
        pass
