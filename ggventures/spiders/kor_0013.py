import scrapy


class Kor0013Spider(scrapy.Spider):
    name = 'kor_0013'
    allowed_domains = ['https://isbs.sogang.ac.kr/']
    start_urls = ['http://https://isbs.sogang.ac.kr//']

    def parse(self, response):
        pass
