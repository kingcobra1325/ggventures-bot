import scrapy


class Kor0008Spider(scrapy.Spider):
    name = 'kor_0008'
    allowed_domains = ['https://www.khu.ac.kr/eng/main/index.do']
    start_urls = ['http://https://www.khu.ac.kr/eng/main/index.do/']

    def parse(self, response):
        pass
