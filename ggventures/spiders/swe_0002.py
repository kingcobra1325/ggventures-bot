import scrapy


class Swe0002Spider(scrapy.Spider):
    name = 'swe_0002'
    allowed_domains = ['https://ju.se/en/about-us/jonkoping-international-business-school.html']
    start_urls = ['http://https://ju.se/en/about-us/jonkoping-international-business-school.html/']

    def parse(self, response):
        pass
