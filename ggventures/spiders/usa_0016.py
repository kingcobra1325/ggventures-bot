import scrapy


class Usa0016Spider(scrapy.Spider):
    name = 'usa_0016'
    allowed_domains = ['https://www.cgu.edu/school/drucker-school-of-management/']
    start_urls = ['http://https://www.cgu.edu/school/drucker-school-of-management//']

    def parse(self, response):
        pass
