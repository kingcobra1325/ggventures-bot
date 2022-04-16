import scrapy


class Zaf0018Spider(scrapy.Spider):
    name = 'zaf_0018'
    allowed_domains = ['https://www.ufs.ac.za/']
    start_urls = ['http://https://www.ufs.ac.za//']

    def parse(self, response):
        pass
