import scrapy


class Kor0007Spider(scrapy.Spider):
    name = 'kor_0007'
    allowed_domains = ['https://biz.korea.ac.kr/eng/main/main.html']
    start_urls = ['http://https://biz.korea.ac.kr/eng/main/main.html/']

    def parse(self, response):
        pass
