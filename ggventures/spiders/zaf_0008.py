import scrapy


class Zaf0008Spider(scrapy.Spider):
    name = 'zaf_0008'
    allowed_domains = ['https://regent.ac.za/']
    start_urls = ['http://https://regent.ac.za//']

    def parse(self, response):
        pass
