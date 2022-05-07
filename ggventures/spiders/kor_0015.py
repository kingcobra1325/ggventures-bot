import scrapy


class Kor0015Spider(scrapy.Spider):
    name = 'kor_0015'
    allowed_domains = ['https://ysb.yonsei.ac.kr/default.asp?lang=e']
    start_urls = ['http://https://ysb.yonsei.ac.kr/default.asp?lang=e/']

    def parse(self, response):
        pass
