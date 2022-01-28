import scrapy


class Gbr0044Spider(scrapy.Spider):
    name = 'gbr_0044'
    allowed_domains = ['https://www.st-andrews.ac.uk/management/']
    start_urls = ['http://https://www.st-andrews.ac.uk/management//']

    def parse(self, response):
        pass
