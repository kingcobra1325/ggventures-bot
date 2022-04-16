import scrapy


class Zaf0016Spider(scrapy.Spider):
    name = 'zaf_0016'
    allowed_domains = ['https://www.gibs.co.za/']
    start_urls = ['http://https://www.gibs.co.za//']

    def parse(self, response):
        pass
