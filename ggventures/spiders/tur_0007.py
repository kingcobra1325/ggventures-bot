import scrapy


class Tur0007Spider(scrapy.Spider):
    name = 'tur_0007'
    allowed_domains = ['https://www.marmara.edu.tr/en/academic/institutes/institute-of-social-sciences']
    start_urls = ['http://https://www.marmara.edu.tr/en/academic/institutes/institute-of-social-sciences/']

    def parse(self, response):
        pass
