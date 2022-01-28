import scrapy


class Gbr0036Spider(scrapy.Spider):
    name = 'gbr_0036'
    allowed_domains = ['https://www.glos.ac.uk/courses/academic-schools/gloucestershire-business-school/']
    start_urls = ['http://https://www.glos.ac.uk/courses/academic-schools/gloucestershire-business-school//']

    def parse(self, response):
        pass
