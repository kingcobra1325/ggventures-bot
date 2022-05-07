import scrapy


class Kor0009Spider(scrapy.Spider):
    name = 'kor_0009'
    allowed_domains = ['https://en.knu.ac.kr/']
    start_urls = ['http://https://en.knu.ac.kr//']

    def parse(self, response):
        pass
