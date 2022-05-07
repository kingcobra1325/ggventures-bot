import scrapy


class Swe0001Spider(scrapy.Spider):
    name = 'swe_0001'
    allowed_domains = ['https://www.gu.se/en/school-business-economics-law']
    start_urls = ['http://https://www.gu.se/en/school-business-economics-law/']

    def parse(self, response):
        pass
