import scrapy


class Kor0012Spider(scrapy.Spider):
    name = 'kor_0012'
    allowed_domains = ['https://cba.snu.ac.kr/en']
    start_urls = ['http://https://cba.snu.ac.kr/en/']

    def parse(self, response):
        pass
