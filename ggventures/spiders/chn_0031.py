import scrapy


class Chn0031Spider(scrapy.Spider):
    name = 'chn_0031'
    allowed_domains = ['http://www.at0086.com/sift/']
    start_urls = ['http://http://www.at0086.com/sift//']

    def parse(self, response):
        pass
