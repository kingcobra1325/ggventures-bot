import scrapy


class Hrv0001Spider(scrapy.Spider):
    name = 'hrv_0001'
    allowed_domains = ['http://www.ub.edu.ph/cba']
    start_urls = ['http://http://www.ub.edu.ph/cba/']

    def parse(self, response):
        pass
