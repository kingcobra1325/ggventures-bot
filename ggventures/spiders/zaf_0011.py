import scrapy


class Zaf0011Spider(scrapy.Spider):
    name = 'zaf_0011'
    allowed_domains = ['https://www.tut.ac.za/']
    start_urls = ['http://https://www.tut.ac.za//']

    def parse(self, response):
        pass
