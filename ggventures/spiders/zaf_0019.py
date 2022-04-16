import scrapy


class Zaf0019Spider(scrapy.Spider):
    name = 'zaf_0019'
    allowed_domains = ['https://www.wbs.ac.za/']
    start_urls = ['http://https://www.wbs.ac.za//']

    def parse(self, response):
        pass
