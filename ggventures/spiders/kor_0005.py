import scrapy


class Kor0005Spider(scrapy.Spider):
    name = 'kor_0005'
    allowed_domains = ['https://www.hanyang.ac.kr/web/eng']
    start_urls = ['http://https://www.hanyang.ac.kr/web/eng/']

    def parse(self, response):
        pass
