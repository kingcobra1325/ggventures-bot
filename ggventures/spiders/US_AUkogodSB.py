import scrapy


class UsAukogodsbSpider(scrapy.Spider):
    name = 'US-AUkogodSB'
    allowed_domains = ['https://kogod.american.edu/']
    start_urls = ['http://https://kogod.american.edu//']

    def parse(self, response):
        pass
