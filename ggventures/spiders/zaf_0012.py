import scrapy


class Zaf0012Spider(scrapy.Spider):
    name = 'zaf_0012'
    allowed_domains = ['https://www.unisa.ac.za/sites/sbl/default/']
    start_urls = ['http://https://www.unisa.ac.za/sites/sbl/default//']

    def parse(self, response):
        pass
