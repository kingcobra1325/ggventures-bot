import scrapy


class Chn0027Spider(scrapy.Spider):
    name = 'chn_0027'
    allowed_domains = ['http://www.studyinqinghai.com/']
    start_urls = ['http://http://www.studyinqinghai.com//']

    def parse(self, response):
        pass
