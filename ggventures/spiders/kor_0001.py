import scrapy


class Kor0001Spider(scrapy.Spider):
    name = 'kor_0001'
    allowed_domains = ['https://www.cbnu.ac.kr/site/english/sub.do?key=491']
    start_urls = ['http://https://www.cbnu.ac.kr/site/english/sub.do?key=491/']

    def parse(self, response):
        pass
