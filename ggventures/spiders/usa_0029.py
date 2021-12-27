import scrapy


class Usa0029Spider(scrapy.Spider):
    name = 'usa_0029'
    allowed_domains = ['https://www.fordham.edu/gabelli-school-of-business/academic-programs-and-admissions/graduate-programs/']
    start_urls = ['http://https://www.fordham.edu/gabelli-school-of-business/academic-programs-and-admissions/graduate-programs//']

    def parse(self, response):
        pass
