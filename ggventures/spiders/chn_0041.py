import scrapy


class Chn0041Spider(scrapy.Spider):
    name = 'chn_0041'
    allowed_domains = ['http://www.studyintibet.com/']
    start_urls = ['http://http://www.studyintibet.com//']

    def parse(self, response):
        pass
