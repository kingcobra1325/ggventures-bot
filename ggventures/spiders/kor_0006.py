import scrapy


class Kor0006Spider(scrapy.Spider):
    name = 'kor_0006'
    allowed_domains = ['https://www.business.kaist.edu/kgsm/']
    start_urls = ['http://https://www.business.kaist.edu/kgsm//']

    def parse(self, response):
        pass
