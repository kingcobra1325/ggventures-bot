import scrapy


class Swe0008Spider(scrapy.Spider):
    name = 'swe_0008'
    allowed_domains = ['https://www.fek.uu.se/?languageId=1']
    start_urls = ['http://https://www.fek.uu.se/?languageId=1/']

    def parse(self, response):
        pass
