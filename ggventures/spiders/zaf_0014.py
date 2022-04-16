import scrapy


class Zaf0014Spider(scrapy.Spider):
    name = 'zaf_0014'
    allowed_domains = ['https://clms.ukzn.ac.za/']
    start_urls = ['http://https://clms.ukzn.ac.za//']

    def parse(self, response):
        pass
