import scrapy


class Usa0027Spider(scrapy.Spider):
    name = 'usa_0027'
    allowed_domains = ['https://www.fairfield.edu/undergraduate/academics/schools-and-colleges/charles-f-dolan-school-of-business/']
    start_urls = ['http://https://www.fairfield.edu/undergraduate/academics/schools-and-colleges/charles-f-dolan-school-of-business//']

    def parse(self, response):
        pass
