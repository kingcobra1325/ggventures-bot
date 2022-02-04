import scrapy


class Aus0005Spider(scrapy.Spider):
    name = 'aus_0005'
    allowed_domains = ['https://study.csu.edu.au/courses/business']
    start_urls = ['http://https://study.csu.edu.au/courses/business/']

    def parse(self, response):
        pass
