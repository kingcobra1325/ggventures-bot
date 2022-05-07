import scrapy


class Kor0010Spider(scrapy.Spider):
    name = 'kor_0010'
    allowed_domains = ['https://biz.pusan.ac.kr/bizeng/14397/subview.do']
    start_urls = ['http://https://biz.pusan.ac.kr/bizeng/14397/subview.do/']

    def parse(self, response):
        pass
