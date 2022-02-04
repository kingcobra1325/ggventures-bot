import scrapy


class Aus0015Spider(scrapy.Spider):
    name = 'aus_0015'
    allowed_domains = ['https://www.qut.edu.au/study/business']
    start_urls = ['http://https://www.qut.edu.au/study/business/']

    def parse(self, response):
        pass
