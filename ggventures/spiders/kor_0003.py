import scrapy


class Kor0003Spider(scrapy.Spider):
    name = 'kor_0003'
    allowed_domains = ['https://plus.cnu.ac.kr/html/en/sub02/sub02_020104.html']
    start_urls = ['http://https://plus.cnu.ac.kr/html/en/sub02/sub02_020104.html/']

    def parse(self, response):
        pass
