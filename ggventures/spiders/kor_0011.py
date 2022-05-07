import scrapy


class Kor0011Spider(scrapy.Spider):
    name = 'kor_0011'
    allowed_domains = ['https://graduatebusiness.sejong.ac.kr/Eng']
    start_urls = ['http://https://graduatebusiness.sejong.ac.kr/Eng/']

    def parse(self, response):
        pass
