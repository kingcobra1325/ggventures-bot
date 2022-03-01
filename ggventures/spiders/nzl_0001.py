import scrapy


class Nzl0001Spider(scrapy.Spider):
    name = 'nzl_0001'
    allowed_domains = ['https://www.aut.ac.nz/about/faculties-and-schools/faculty-of-business,-economics-and-law']
    start_urls = ['http://https://www.aut.ac.nz/about/faculties-and-schools/faculty-of-business,-economics-and-law/']

    def parse(self, response):
        pass
