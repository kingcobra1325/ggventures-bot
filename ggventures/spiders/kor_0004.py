import scrapy


class Kor0004Spider(scrapy.Spider):
    name = 'kor_0004'
    allowed_domains = ['http://biz.ewha.ac.kr/eng/']
    start_urls = ['http://http://biz.ewha.ac.kr/eng//']

    def parse(self, response):
        pass
