import scrapy


class Aus0018Spider(scrapy.Spider):
    name = 'aus_0018'
    allowed_domains = ['https://www.westernsydney.edu.au/future/study/courses/sydney-graduate-school-of-management']
    start_urls = ['http://https://www.westernsydney.edu.au/future/study/courses/sydney-graduate-school-of-management/']

    def parse(self, response):
        pass
