import scrapy


class Zaf0005Spider(scrapy.Spider):
    name = 'zaf_0005'
    allowed_domains = ['http://businessschool.mandela.ac.za/']
    start_urls = ['http://http://businessschool.mandela.ac.za//']

    def parse(self, response):
        pass
