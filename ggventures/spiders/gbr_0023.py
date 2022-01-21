import scrapy


class Gbr0023Spider(scrapy.Spider):
    name = 'gbr_0023'
    allowed_domains = ['https://www.northumbria.ac.uk/about-us/academic-departments/newcastle-business-school/']
    start_urls = ['http://https://www.northumbria.ac.uk/about-us/academic-departments/newcastle-business-school//']

    def parse(self, response):
        pass
