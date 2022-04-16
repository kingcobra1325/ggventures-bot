import scrapy


class Zaf0006Spider(scrapy.Spider):
    name = 'zaf_0006'
    allowed_domains = ['https://commerce.nwu.ac.za/']
    start_urls = ['http://https://commerce.nwu.ac.za//']

    def parse(self, response):
        pass
