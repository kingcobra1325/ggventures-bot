import scrapy


class Gbr0037Spider(scrapy.Spider):
    name = 'gbr_0037'
    allowed_domains = ['https://www.hull.ac.uk/faculties/fblp/hull-university-business-school']
    start_urls = ['http://https://www.hull.ac.uk/faculties/fblp/hull-university-business-school/']

    def parse(self, response):
        pass
