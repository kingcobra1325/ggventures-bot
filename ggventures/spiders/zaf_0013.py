import scrapy


class Zaf0013Spider(scrapy.Spider):
    name = 'zaf_0013'
    allowed_domains = ['https://www.gsb.uct.ac.za/']
    start_urls = ['http://https://www.gsb.uct.ac.za//']

    def parse(self, response):
        pass
