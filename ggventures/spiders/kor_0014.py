import scrapy


class Kor0014Spider(scrapy.Spider):
    name = 'kor_0014'
    allowed_domains = ['https://gsb.skku.edu/en/index.do']
    start_urls = ['http://https://gsb.skku.edu/en/index.do/']

    def parse(self, response):
        pass
